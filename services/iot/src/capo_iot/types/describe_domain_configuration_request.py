"""Generated from Smithy shape ``com.amazonaws.iot#DescribeDomainConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.reserved_domain_configuration_name


class DescribeDomainConfigurationRequest(TypedDict, closed=True):
    domain_configuration_name: "capo_iot.types.reserved_domain_configuration_name.ReservedDomainConfigurationName"
    """<p>The name of the domain configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDomainConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDomainConfigurationRequest:
    out: DescribeDomainConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
