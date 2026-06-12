"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListNotificationsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.list_notifications_max_results
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.resource_arn
    import aws_sdk_wellarchitected.types.workload_id


class ListNotificationsInput(TypedDict):
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired[
        "aws_sdk_wellarchitected.types.list_notifications_max_results.ListNotificationsMaxResults"
    ]
    """<p>The maximum number of results to return for this request.</p>"""
    resource_arn: NotRequired["aws_sdk_wellarchitected.types.resource_arn.ResourceArn"]
    """<p>The ARN for the related resource for the notification.</p> <note> <p>Only one of <code>WorkloadID</code> or <code>ResourceARN</code> should be specified.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationsInput) -> dict:
    out: dict = {}
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> ListNotificationsInput:
    out: ListNotificationsInput = {}  # type: ignore[typeddict-item]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    return out
