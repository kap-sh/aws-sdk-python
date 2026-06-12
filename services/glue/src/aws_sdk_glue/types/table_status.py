"""Generated from Smithy shape ``com.amazonaws.glue#TableStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.error_detail
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.resource_action
    import aws_sdk_glue.types.resource_state
    import aws_sdk_glue.types.status_details
    import aws_sdk_glue.types.timestamp


class TableStatus(TypedDict):
    requested_by: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The ARN of the user who requested the asynchronous change.</p>"""
    updated_by: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The ARN of the user to last manually alter the asynchronous change (requesting cancellation, etc).</p>"""
    request_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>An ISO 8601 formatted date string indicating the time that the change was initiated.</p>"""
    update_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>An ISO 8601 formatted date string indicating the time that the state was last updated.</p>"""
    action: NotRequired["aws_sdk_glue.types.resource_action.ResourceAction"]
    """<p>Indicates which action was called on the table, currently only <code>CREATE</code> or <code>UPDATE</code>.</p>"""
    state: NotRequired["aws_sdk_glue.types.resource_state.ResourceState"]
    """<p>A generic status for the change in progress, such as QUEUED, IN_PROGRESS, SUCCESS, or FAILED.</p>"""
    error: NotRequired["aws_sdk_glue.types.error_detail.ErrorDetail"]
    """<p>An error that will only appear when the state is \"FAILED\". This is a parent level exception message, there may be different <code>Error</code>s for each dialect.</p>"""
    details: NotRequired["aws_sdk_glue.types.status_details.StatusDetails"]
    """<p>A <code>StatusDetails</code> object with information about the requested change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableStatus) -> dict:
    out: dict = {}
    if "requested_by" in value:
        out["RequestedBy"] = value["requested_by"]
    if "updated_by" in value:
        out["UpdatedBy"] = value["updated_by"]
    if "request_time" in value:
        import aws_sdk_glue.types.timestamp

        out["RequestTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["request_time"]
        )
    if "update_time" in value:
        import aws_sdk_glue.types.timestamp

        out["UpdateTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["update_time"]
        )
    if "action" in value:
        import aws_sdk_glue.types.resource_action

        out["Action"] = aws_sdk_glue.types.resource_action.serialize_aws_json_1_1(
            value["action"]
        )
    if "state" in value:
        import aws_sdk_glue.types.resource_state

        out["State"] = aws_sdk_glue.types.resource_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "error" in value:
        import aws_sdk_glue.types.error_detail

        out["Error"] = aws_sdk_glue.types.error_detail.serialize_aws_json_1_1(
            value["error"]
        )
    if "details" in value:
        import aws_sdk_glue.types.status_details

        out["Details"] = aws_sdk_glue.types.status_details.serialize_aws_json_1_1(
            value["details"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TableStatus:
    out: TableStatus = {}  # type: ignore[typeddict-item]
    if "RequestedBy" in data:
        out["requested_by"] = data["RequestedBy"]
    if "UpdatedBy" in data:
        out["updated_by"] = data["UpdatedBy"]
    if "RequestTime" in data:
        import aws_sdk_glue.types.timestamp

        out["request_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["RequestTime"]
        )
    if "UpdateTime" in data:
        import aws_sdk_glue.types.timestamp

        out["update_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["UpdateTime"]
        )
    if "Action" in data:
        import aws_sdk_glue.types.resource_action

        out["action"] = aws_sdk_glue.types.resource_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    if "State" in data:
        import aws_sdk_glue.types.resource_state

        out["state"] = aws_sdk_glue.types.resource_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "Error" in data:
        import aws_sdk_glue.types.error_detail

        out["error"] = aws_sdk_glue.types.error_detail.deserialize_aws_json_1_1(
            data["Error"]
        )
    if "Details" in data:
        import aws_sdk_glue.types.status_details

        out["details"] = aws_sdk_glue.types.status_details.deserialize_aws_json_1_1(
            data["Details"]
        )
    return out
