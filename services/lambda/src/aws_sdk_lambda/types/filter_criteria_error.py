"""Generated from Smithy shape ``com.amazonaws.lambda#FilterCriteriaError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.filter_criteria_error_code
    import aws_sdk_lambda.types.filter_criteria_error_message


class FilterCriteriaError(TypedDict):
    error_code: NotRequired[
        "aws_sdk_lambda.types.filter_criteria_error_code.FilterCriteriaErrorCode"
    ]
    """<p>The KMS exception that resulted from filter criteria encryption or decryption.</p>"""
    message: NotRequired[
        "aws_sdk_lambda.types.filter_criteria_error_message.FilterCriteriaErrorMessage"
    ]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCriteriaError) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> FilterCriteriaError:
    out: FilterCriteriaError = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
