"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetResourceConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.resource_configuration_identifier


class GetResourceConfigurationRequest(TypedDict):
    resource_configuration_identifier: "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
    """<p>The ID of the resource configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourceConfigurationRequest:
    out: GetResourceConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
