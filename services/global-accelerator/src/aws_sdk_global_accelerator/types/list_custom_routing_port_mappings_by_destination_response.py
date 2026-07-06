"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListCustomRoutingPortMappingsByDestinationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.destination_port_mappings
    import aws_sdk_global_accelerator.types.generic_string


class ListCustomRoutingPortMappingsByDestinationResponse(TypedDict, closed=True):
    destination_port_mappings: NotRequired[
        "aws_sdk_global_accelerator.types.destination_port_mappings.DestinationPortMappings"
    ]
    """<p>The port mappings for the endpoint IP address that you specified in the request.</p>"""
    next_token: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListCustomRoutingPortMappingsByDestinationResponse,
) -> dict:
    out: dict = {}
    if "destination_port_mappings" in value:
        import aws_sdk_global_accelerator.types.destination_port_mappings

        out["DestinationPortMappings"] = (
            aws_sdk_global_accelerator.types.destination_port_mappings.serialize_aws_json_1_1(
                value["destination_port_mappings"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListCustomRoutingPortMappingsByDestinationResponse:
    out: ListCustomRoutingPortMappingsByDestinationResponse = {}  # type: ignore[typeddict-item]
    if "DestinationPortMappings" in data:
        import aws_sdk_global_accelerator.types.destination_port_mappings

        out["destination_port_mappings"] = (
            aws_sdk_global_accelerator.types.destination_port_mappings.deserialize_aws_json_1_1(
                data["DestinationPortMappings"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
