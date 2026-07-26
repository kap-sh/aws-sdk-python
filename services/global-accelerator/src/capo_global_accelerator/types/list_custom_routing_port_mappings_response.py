"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListCustomRoutingPortMappingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.port_mappings


class ListCustomRoutingPortMappingsResponse(TypedDict, closed=True):
    port_mappings: NotRequired[
        "capo_global_accelerator.types.port_mappings.PortMappings"
    ]
    """<p>The port mappings for a custom routing accelerator.</p>"""
    next_token: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCustomRoutingPortMappingsResponse) -> dict:
    out: dict = {}
    if "port_mappings" in value:
        import capo_global_accelerator.types.port_mappings

        out["PortMappings"] = (
            capo_global_accelerator.types.port_mappings.serialize_aws_json_1_1(
                value["port_mappings"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCustomRoutingPortMappingsResponse:
    out: ListCustomRoutingPortMappingsResponse = {}  # type: ignore[typeddict-item]
    if "PortMappings" in data:
        import capo_global_accelerator.types.port_mappings

        out["port_mappings"] = (
            capo_global_accelerator.types.port_mappings.deserialize_aws_json_1_1(
                data["PortMappings"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
