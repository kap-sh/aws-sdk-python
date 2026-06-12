"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteResourceConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.resource_configuration_identifier


class DeleteResourceConfigurationRequest(TypedDict):
    resource_configuration_identifier: "aws_sdk_vpc_lattice.types.resource_configuration_identifier.ResourceConfigurationIdentifier"
    """<p>The ID or ARN of the resource configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourceConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourceConfigurationRequest:
    out: DeleteResourceConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
