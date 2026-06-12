"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeNotificationSubscriptionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.page_marker_type
    import aws_sdk_workdocs.types.subscription_list


class DescribeNotificationSubscriptionsResponse(TypedDict):
    subscriptions: NotRequired[
        "aws_sdk_workdocs.types.subscription_list.SubscriptionList"
    ]
    """<p>The subscriptions.</p>"""
    marker: NotRequired["aws_sdk_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker to use when requesting the next set of results. If there are no additional results, the string is empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNotificationSubscriptionsResponse) -> dict:
    out: dict = {}
    if "subscriptions" in value:
        import aws_sdk_workdocs.types.subscription_list

        out["Subscriptions"] = aws_sdk_workdocs.types.subscription_list.serialize_json(
            value["subscriptions"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> DescribeNotificationSubscriptionsResponse:
    out: DescribeNotificationSubscriptionsResponse = {}  # type: ignore[typeddict-item]
    if "Subscriptions" in data:
        import aws_sdk_workdocs.types.subscription_list

        out["subscriptions"] = (
            aws_sdk_workdocs.types.subscription_list.deserialize_json(
                data["Subscriptions"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
