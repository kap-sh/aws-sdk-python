"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeNotificationSubscriptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.limit_type
    import aws_sdk_workdocs.types.page_marker_type


class DescribeNotificationSubscriptionsRequest(TypedDict):
    organization_id: "aws_sdk_workdocs.types.id_type.IdType"
    """<p>The ID of the organization.</p>"""
    marker: NotRequired["aws_sdk_workdocs.types.page_marker_type.PageMarkerType"]
    """<p>The marker for the next set of results. (You received this marker from a previous call.)</p>"""
    limit: NotRequired["aws_sdk_workdocs.types.limit_type.LimitType"]
    """<p>The maximum number of items to return with this call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNotificationSubscriptionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeNotificationSubscriptionsRequest:
    out: DescribeNotificationSubscriptionsRequest = {}  # type: ignore[typeddict-item]
    return out
