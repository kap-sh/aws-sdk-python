"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExecutionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bcm_data_exports.types.execution_status_code
    import capo_bcm_data_exports.types.execution_status_reason


class ExecutionStatus(TypedDict, closed=True):
    status_code: NotRequired[
        "capo_bcm_data_exports.types.execution_status_code.ExecutionStatusCode"
    ]
    """<p>The code for the status of the execution.</p>"""
    status_reason: NotRequired[
        "capo_bcm_data_exports.types.execution_status_reason.ExecutionStatusReason"
    ]
    """<p>The reason for the failed status.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time when the execution was created.</p>"""
    completed_at: NotRequired["datetime.datetime"]
    """<p>The time when the execution was completed.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The time when the execution was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionStatus) -> dict:
    out: dict = {}
    if "status_code" in value:
        import capo_bcm_data_exports.types.execution_status_code

        out["StatusCode"] = (
            capo_bcm_data_exports.types.execution_status_code.serialize_aws_json_1_1(
                value["status_code"]
            )
        )
    if "status_reason" in value:
        import capo_bcm_data_exports.types.execution_status_reason

        out["StatusReason"] = (
            capo_bcm_data_exports.types.execution_status_reason.serialize_aws_json_1_1(
                value["status_reason"]
            )
        )
    if "created_at" in value:
        import capo_bcm_data_exports.types._prelude.timestamp

        out["CreatedAt"] = (
            capo_bcm_data_exports.types._prelude.timestamp.serialize_aws_json_1_1(
                value["created_at"]
            )
        )
    if "completed_at" in value:
        import capo_bcm_data_exports.types._prelude.timestamp

        out["CompletedAt"] = (
            capo_bcm_data_exports.types._prelude.timestamp.serialize_aws_json_1_1(
                value["completed_at"]
            )
        )
    if "last_updated_at" in value:
        import capo_bcm_data_exports.types._prelude.timestamp

        out["LastUpdatedAt"] = (
            capo_bcm_data_exports.types._prelude.timestamp.serialize_aws_json_1_1(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionStatus:
    out: ExecutionStatus = {}  # type: ignore[typeddict-item]
    if "StatusCode" in data:
        import capo_bcm_data_exports.types.execution_status_code

        out["status_code"] = (
            capo_bcm_data_exports.types.execution_status_code.deserialize_aws_json_1_1(
                data["StatusCode"]
            )
        )
    if "StatusReason" in data:
        import capo_bcm_data_exports.types.execution_status_reason

        out["status_reason"] = (
            capo_bcm_data_exports.types.execution_status_reason.deserialize_aws_json_1_1(
                data["StatusReason"]
            )
        )
    if "CreatedAt" in data:
        import capo_bcm_data_exports.types._prelude.timestamp

        out["created_at"] = (
            capo_bcm_data_exports.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["CreatedAt"]
            )
        )
    if "CompletedAt" in data:
        import capo_bcm_data_exports.types._prelude.timestamp

        out["completed_at"] = (
            capo_bcm_data_exports.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["CompletedAt"]
            )
        )
    if "LastUpdatedAt" in data:
        import capo_bcm_data_exports.types._prelude.timestamp

        out["last_updated_at"] = (
            capo_bcm_data_exports.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedAt"]
            )
        )
    return out
