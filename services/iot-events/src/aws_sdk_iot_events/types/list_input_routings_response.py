"""Generated from Smithy shape ``com.amazonaws.iotevents#ListInputRoutingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.next_token
    import aws_sdk_iot_events.types.routed_resources


class ListInputRoutingsResponse(TypedDict):
    routed_resources: NotRequired[
        "aws_sdk_iot_events.types.routed_resources.RoutedResources"
    ]
    """<p> Summary information about the routed resources. </p>"""
    next_token: NotRequired["aws_sdk_iot_events.types.next_token.NextToken"]
    """<p> The token that you can use to return the next set of results, or <code>null</code> if there are no more results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInputRoutingsResponse) -> dict:
    out: dict = {}
    if "routed_resources" in value:
        import aws_sdk_iot_events.types.routed_resources

        out["routedResources"] = (
            aws_sdk_iot_events.types.routed_resources.serialize_json(
                value["routed_resources"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInputRoutingsResponse:
    out: ListInputRoutingsResponse = {}  # type: ignore[typeddict-item]
    if "routedResources" in data:
        import aws_sdk_iot_events.types.routed_resources

        out["routed_resources"] = (
            aws_sdk_iot_events.types.routed_resources.deserialize_json(
                data["routedResources"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
