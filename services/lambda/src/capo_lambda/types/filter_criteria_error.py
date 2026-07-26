"""Generated from Smithy shape ``com.amazonaws.lambda#FilterCriteriaError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.filter_criteria_error_code
    import capo_lambda.types.filter_criteria_error_message


class FilterCriteriaError(TypedDict, closed=True):
    error_code: NotRequired[
        "capo_lambda.types.filter_criteria_error_code.FilterCriteriaErrorCode"
    ]
    """<p>The KMS exception that resulted from filter criteria encryption or decryption.</p>"""
    message: NotRequired[
        "capo_lambda.types.filter_criteria_error_message.FilterCriteriaErrorMessage"
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
