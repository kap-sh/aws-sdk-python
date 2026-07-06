"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListCustomRoutingListenersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_listeners
    import aws_sdk_global_accelerator.types.generic_string


class ListCustomRoutingListenersResponse(TypedDict, closed=True):
    listeners: NotRequired[
        "aws_sdk_global_accelerator.types.custom_routing_listeners.CustomRoutingListeners"
    ]
    """<p>The list of listeners for a custom routing accelerator.</p>"""
    next_token: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCustomRoutingListenersResponse) -> dict:
    out: dict = {}
    if "listeners" in value:
        import aws_sdk_global_accelerator.types.custom_routing_listeners

        out["Listeners"] = (
            aws_sdk_global_accelerator.types.custom_routing_listeners.serialize_aws_json_1_1(
                value["listeners"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCustomRoutingListenersResponse:
    out: ListCustomRoutingListenersResponse = {}  # type: ignore[typeddict-item]
    if "Listeners" in data:
        import aws_sdk_global_accelerator.types.custom_routing_listeners

        out["listeners"] = (
            aws_sdk_global_accelerator.types.custom_routing_listeners.deserialize_aws_json_1_1(
                data["Listeners"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
