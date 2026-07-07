"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetCoreNetworkChangeEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_change_event_list
    import aws_sdk_networkmanager.types.next_token


class GetCoreNetworkChangeEventsResponse(TypedDict, closed=True):
    core_network_change_events: NotRequired[
        "aws_sdk_networkmanager.types.core_network_change_event_list.CoreNetworkChangeEventList"
    ]
    """<p>The response to <code>GetCoreNetworkChangeEventsRequest</code>.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCoreNetworkChangeEventsResponse) -> dict:
    out: dict = {}
    if "core_network_change_events" in value:
        import aws_sdk_networkmanager.types.core_network_change_event_list

        out["CoreNetworkChangeEvents"] = (
            aws_sdk_networkmanager.types.core_network_change_event_list.serialize_json(
                value["core_network_change_events"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetCoreNetworkChangeEventsResponse:
    out: GetCoreNetworkChangeEventsResponse = {}  # type: ignore[typeddict-item]
    if "CoreNetworkChangeEvents" in data:
        import aws_sdk_networkmanager.types.core_network_change_event_list

        out["core_network_change_events"] = (
            aws_sdk_networkmanager.types.core_network_change_event_list.deserialize_json(
                data["CoreNetworkChangeEvents"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
