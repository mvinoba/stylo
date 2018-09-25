import pytest

from stylo.domain import RealDomain
from stylo.domain.transform import RealDomainTransform
from stylo.domain.transform.translation import Translation
from stylo.domain.transform.transform import find_base_transform, find_base_domain
from stylo.shape import Circle


@pytest.mark.domain
class TestFindBaseTransform:
    """Tests for the :code:`find_base_transform` function."""

    def test_with_transform(self):
        """Ensure that when given a domain transform, this function returns the
        appropriate base class."""

        base_transform = find_base_transform(Translation)
        assert base_transform == RealDomainTransform

    def test_with_shape(self):
        """Ensure that when given something that is not a domain transform, this
        function raises the appropriate exception"""

        with pytest.raises(TypeError) as err:
            find_base_transform(Circle)

        assert "is not a domain transform" in str(err.value)


@pytest.mark.domain
class TestFindBaseDomain:
    """Tests for the :code:`find_base_domain` function."""

    def test_with_base_transform(self):
        """Ensure that when given a base domain transform, this function performs as
        expected."""

        base_domain = find_base_domain(RealDomainTransform)
        assert base_domain == RealDomain

    def test_with_shape(self):
        """Ensure that when given something that is not a domain, this function raises
        the appropriate exception."""

        with pytest.raises(TypeError) as err:
            find_base_domain(Circle)

        assert "is not a base domain transform" in str(err.value)

    def test_with_transform(self):
        """Ensure that when given a transform that is not the base this raises the
        appropriate exception."""

        with pytest.raises(TypeError) as err:
            find_base_domain(Translation)

        assert "is not a base domain transform" in str(err.value)
