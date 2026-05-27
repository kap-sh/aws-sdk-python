"""Generated from Smithy shape ``com.amazonaws.lambda#TagsError``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.tags_error_code
    import aws_sdk_lambda.types.tags_error_message


class TagsError(TypedDict):
    error_code: "aws_sdk_lambda.types.tags_error_code.TagsErrorCode"
    """<p>The error code.</p>"""
    message: "aws_sdk_lambda.types.tags_error_message.TagsErrorMessage"
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagsError) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TagsError:
    out: TagsError = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("TagsError.error_code required")
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("TagsError.message required")
    return out
