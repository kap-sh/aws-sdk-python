"""Generated from Smithy shape ``com.amazonaws.wickr#BatchUnameErrorResponseItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.uname


class BatchUnameErrorResponseItem(TypedDict):
    field: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The field that caused the error.</p>"""
    reason: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A description of why the username hash lookup failed.</p>"""
    uname: "aws_sdk_wickr.types.uname.Uname"
    """<p>The username hash that failed to be looked up.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUnameErrorResponseItem) -> dict:
    out: dict = {}
    if "field" in value:
        out["field"] = value["field"]
    if "reason" in value:
        out["reason"] = value["reason"]
    out["uname"] = value["uname"]
    return out


def deserialize_json(data: dict) -> BatchUnameErrorResponseItem:
    out: BatchUnameErrorResponseItem = {}  # type: ignore[typeddict-item]
    if "field" in data:
        out["field"] = data["field"]
    if "reason" in data:
        out["reason"] = data["reason"]
    if "uname" in data:
        out["uname"] = data["uname"]
    else:
        raise DeserializationError("BatchUnameErrorResponseItem.uname required")
    return out
