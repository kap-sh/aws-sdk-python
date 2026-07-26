"""Generated from Smithy shape ``com.amazonaws.iot#DeleteDomainConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.domain_configuration_name


class DeleteDomainConfigurationRequest(TypedDict, closed=True):
    domain_configuration_name: (
        "capo_iot.types.domain_configuration_name.DomainConfigurationName"
    )
    """<p>The name of the domain configuration to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainConfigurationRequest:
    out: DeleteDomainConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
