"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupingStatusesItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.error_code
    import capo_resource_groups.types.error_message
    import capo_resource_groups.types.grouping_status
    import capo_resource_groups.types.grouping_type
    import capo_resource_groups.types.resource_arn
    import capo_resource_groups.types.timestamp


class GroupingStatusesItem(TypedDict, closed=True):
    resource_arn: NotRequired["capo_resource_groups.types.resource_arn.ResourceArn"]
    """<p>The Amazon resource name (ARN) of a resource. </p>"""
    action: NotRequired["capo_resource_groups.types.grouping_type.GroupingType"]
    """<p>Describes the resource grouping action with values of <code>GROUP</code> or <code>UNGROUP</code>. </p>"""
    status: NotRequired["capo_resource_groups.types.grouping_status.GroupingStatus"]
    """<p>Describes the resource grouping status with values of <code>SUCCESS</code>, <code>FAILED</code>, <code>IN_PROGRESS</code>, or <code>SKIPPED</code>. </p>"""
    error_message: NotRequired["capo_resource_groups.types.error_message.ErrorMessage"]
    """<p>A message that explains the <code>ErrorCode</code>. </p>"""
    error_code: NotRequired["capo_resource_groups.types.error_code.ErrorCode"]
    """<p>Specifies the error code that was raised. </p>"""
    updated_at: NotRequired["capo_resource_groups.types.timestamp.timestamp"]
    """<p>A timestamp of when the status was last updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupingStatusesItem) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "action" in value:
        import capo_resource_groups.types.grouping_type

        out["Action"] = capo_resource_groups.types.grouping_type.serialize_json(
            value["action"]
        )
    if "status" in value:
        import capo_resource_groups.types.grouping_status

        out["Status"] = capo_resource_groups.types.grouping_status.serialize_json(
            value["status"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "updated_at" in value:
        import capo_resource_groups.types.timestamp

        out["UpdatedAt"] = capo_resource_groups.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GroupingStatusesItem:
    out: GroupingStatusesItem = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Action" in data:
        import capo_resource_groups.types.grouping_type

        out["action"] = capo_resource_groups.types.grouping_type.deserialize_json(
            data["Action"]
        )
    if "Status" in data:
        import capo_resource_groups.types.grouping_status

        out["status"] = capo_resource_groups.types.grouping_status.deserialize_json(
            data["Status"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "UpdatedAt" in data:
        import capo_resource_groups.types.timestamp

        out["updated_at"] = capo_resource_groups.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
