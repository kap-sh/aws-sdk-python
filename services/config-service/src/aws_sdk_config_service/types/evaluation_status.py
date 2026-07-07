"""Generated from Smithy shape ``com.amazonaws.configservice#EvaluationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.resource_evaluation_status
    import aws_sdk_config_service.types.string_with_char_limit1024


class EvaluationStatus(TypedDict, closed=True):
    status: "aws_sdk_config_service.types.resource_evaluation_status.ResourceEvaluationStatus"
    """<p>The status of an execution. The valid values are In_Progress, Succeeded or Failed. </p>"""
    failure_reason: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit1024.StringWithCharLimit1024"
    ]
    """<p>An explanation for failed execution status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationStatus) -> dict:
    out: dict = {}
    import aws_sdk_config_service.types.resource_evaluation_status

    out["Status"] = (
        aws_sdk_config_service.types.resource_evaluation_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluationStatus:
    out: EvaluationStatus = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_config_service.types.resource_evaluation_status

        out["status"] = (
            aws_sdk_config_service.types.resource_evaluation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("EvaluationStatus.status required")
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
