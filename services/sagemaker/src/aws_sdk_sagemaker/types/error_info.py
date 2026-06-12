"""Generated from Smithy shape ``com.amazonaws.sagemaker#ErrorInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.non_empty_string64
    import aws_sdk_sagemaker.types.non_empty_string256


class ErrorInfo(TypedDict):
    code: NotRequired["aws_sdk_sagemaker.types.non_empty_string64.NonEmptyString64"]
    """<p>The error code for an invalid or failed operation.</p>"""
    reason: NotRequired["aws_sdk_sagemaker.types.non_empty_string256.NonEmptyString256"]
    """<p>The failure reason for the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorInfo) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ErrorInfo:
    out: ErrorInfo = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out
