"""Generated from Smithy shape ``com.amazonaws.apprunner#OperationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.operation_status
    import capo_apprunner.types.operation_type
    import capo_apprunner.types.timestamp
    import capo_apprunner.types.uuid


class OperationSummary(TypedDict, closed=True):
    id: NotRequired["capo_apprunner.types.uuid.UUID"]
    """<p>A unique ID of this operation. It's unique in the scope of the App Runner service.</p>"""
    type: NotRequired["capo_apprunner.types.operation_type.OperationType"]
    """<p>The type of operation. It indicates a specific action that occured.</p>"""
    status: NotRequired["capo_apprunner.types.operation_status.OperationStatus"]
    """<p>The current state of the operation.</p>"""
    target_arn: NotRequired[
        "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource that the operation acted on (for example, an App Runner service).</p>"""
    started_at: NotRequired["capo_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the operation started. It's in the Unix time stamp format.</p>"""
    ended_at: NotRequired["capo_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the operation ended. It's in the Unix time stamp format.</p>"""
    updated_at: NotRequired["capo_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the operation was last updated. It's in the Unix time stamp format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OperationSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import capo_apprunner.types.operation_type

        out["Type"] = capo_apprunner.types.operation_type.serialize_aws_json_1_0(
            value["type"]
        )
    if "status" in value:
        import capo_apprunner.types.operation_status

        out["Status"] = capo_apprunner.types.operation_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "target_arn" in value:
        out["TargetArn"] = value["target_arn"]
    if "started_at" in value:
        import capo_apprunner.types.timestamp

        out["StartedAt"] = capo_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["started_at"]
        )
    if "ended_at" in value:
        import capo_apprunner.types.timestamp

        out["EndedAt"] = capo_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["ended_at"]
        )
    if "updated_at" in value:
        import capo_apprunner.types.timestamp

        out["UpdatedAt"] = capo_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OperationSummary:
    out: OperationSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Type" in data:
        import capo_apprunner.types.operation_type

        out["type"] = capo_apprunner.types.operation_type.deserialize_aws_json_1_0(
            data["Type"]
        )
    if "Status" in data:
        import capo_apprunner.types.operation_status

        out["status"] = capo_apprunner.types.operation_status.deserialize_aws_json_1_0(
            data["Status"]
        )
    if "TargetArn" in data:
        out["target_arn"] = data["TargetArn"]
    if "StartedAt" in data:
        import capo_apprunner.types.timestamp

        out["started_at"] = capo_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["StartedAt"]
        )
    if "EndedAt" in data:
        import capo_apprunner.types.timestamp

        out["ended_at"] = capo_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["EndedAt"]
        )
    if "UpdatedAt" in data:
        import capo_apprunner.types.timestamp

        out["updated_at"] = capo_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["UpdatedAt"]
        )
    return out
