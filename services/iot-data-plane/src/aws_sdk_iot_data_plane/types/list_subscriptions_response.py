"""Generated from Smithy shape ``com.amazonaws.iotdataplane#ListSubscriptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_data_plane.types.next_token
    import aws_sdk_iot_data_plane.types.subscription_list


class ListSubscriptionsResponse(TypedDict, closed=True):
    subscriptions: NotRequired[
        "aws_sdk_iot_data_plane.types.subscription_list.SubscriptionList"
    ]
    """<p>A list of topic filters and their associated Quality of Service (QoS) levels that the client is subscribed to.</p>"""
    next_token: NotRequired["aws_sdk_iot_data_plane.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscriptionsResponse) -> dict:
    out: dict = {}
    if "subscriptions" in value:
        import aws_sdk_iot_data_plane.types.subscription_list

        out["subscriptions"] = (
            aws_sdk_iot_data_plane.types.subscription_list.serialize_json(
                value["subscriptions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSubscriptionsResponse:
    out: ListSubscriptionsResponse = {}  # type: ignore[typeddict-item]
    if "subscriptions" in data:
        import aws_sdk_iot_data_plane.types.subscription_list

        out["subscriptions"] = (
            aws_sdk_iot_data_plane.types.subscription_list.deserialize_json(
                data["subscriptions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
