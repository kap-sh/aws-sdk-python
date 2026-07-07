"""Generated from Smithy shape ``com.amazonaws.sagemaker#LastUpdateStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.last_update_status_value


class LastUpdateStatus(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_sagemaker.types.last_update_status_value.LastUpdateStatusValue"
    ]
    """<p>A value that indicates whether the update was made successful.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the update wasn't successful, indicates the reason why it failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastUpdateStatus) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sagemaker.types.last_update_status_value

        out["Status"] = (
            aws_sdk_sagemaker.types.last_update_status_value.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LastUpdateStatus:
    out: LastUpdateStatus = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sagemaker.types.last_update_status_value

        out["status"] = (
            aws_sdk_sagemaker.types.last_update_status_value.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
