"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ExecutionErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.non_empty_string


class ExecutionErrorDetails(TypedDict, closed=True):
    error_code: "aws_sdk_lex_models_v2.types.non_empty_string.NonEmptyString"
    """<p>The error code for the error.</p>"""
    error_message: "aws_sdk_lex_models_v2.types.non_empty_string.NonEmptyString"
    """<p>The message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionErrorDetails) -> dict:
    out: dict = {}
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ExecutionErrorDetails:
    out: ExecutionErrorDetails = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("ExecutionErrorDetails.error_code required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError("ExecutionErrorDetails.error_message required")
    return out
