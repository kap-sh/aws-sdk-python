"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#OperationFailureDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.error_info
    import capo_kinesis_analytics_v2.types.operation_id


class OperationFailureDetails(TypedDict, closed=True):
    rollback_operation_id: NotRequired[
        "capo_kinesis_analytics_v2.types.operation_id.OperationId"
    ]
    """<p>The rollback operation ID of the system-rollback operation that executed due to failure in the current operation.</p>"""
    error_info: NotRequired["capo_kinesis_analytics_v2.types.error_info.ErrorInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationFailureDetails) -> dict:
    out: dict = {}
    if "rollback_operation_id" in value:
        out["RollbackOperationId"] = value["rollback_operation_id"]
    if "error_info" in value:
        import capo_kinesis_analytics_v2.types.error_info

        out["ErrorInfo"] = (
            capo_kinesis_analytics_v2.types.error_info.serialize_aws_json_1_1(
                value["error_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OperationFailureDetails:
    out: OperationFailureDetails = {}  # type: ignore[typeddict-item]
    if "RollbackOperationId" in data:
        out["rollback_operation_id"] = data["RollbackOperationId"]
    if "ErrorInfo" in data:
        import capo_kinesis_analytics_v2.types.error_info

        out["error_info"] = (
            capo_kinesis_analytics_v2.types.error_info.deserialize_aws_json_1_1(
                data["ErrorInfo"]
            )
        )
    return out
