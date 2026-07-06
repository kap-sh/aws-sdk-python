"""Generated from Smithy shape ``com.amazonaws.wickr#BatchUserErrorResponseItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.user_id


class BatchUserErrorResponseItem(TypedDict, closed=True):
    field: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The field that caused the error.</p>"""
    reason: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A description of why the user operation failed.</p>"""
    user_id: "aws_sdk_wickr.types.user_id.UserId"
    """<p>The user ID associated with the failed operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUserErrorResponseItem) -> dict:
    out: dict = {}
    if "field" in value:
        out["field"] = value["field"]
    if "reason" in value:
        out["reason"] = value["reason"]
    out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> BatchUserErrorResponseItem:
    out: BatchUserErrorResponseItem = {}  # type: ignore[typeddict-item]
    if "field" in data:
        out["field"] = data["field"]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("BatchUserErrorResponseItem.user_id required")
    return out
