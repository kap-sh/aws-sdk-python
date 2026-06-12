"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsLambdaFunctionEnvironmentError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsLambdaFunctionEnvironmentError(TypedDict):
    error_code: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The error code.</p>"""
    message: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsLambdaFunctionEnvironmentError) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AwsLambdaFunctionEnvironmentError:
    out: AwsLambdaFunctionEnvironmentError = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
