"""Generated from Smithy shape ``com.amazonaws.wickr#BatchUnameSuccessResponseItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.uname


class BatchUnameSuccessResponseItem(TypedDict, closed=True):
    uname: "aws_sdk_wickr.types.uname.Uname"
    """<p>The username hash that was successfully resolved.</p>"""
    username: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The email address or username corresponding to the username hash.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUnameSuccessResponseItem) -> dict:
    out: dict = {}
    out["uname"] = value["uname"]
    out["username"] = value["username"]
    return out


def deserialize_json(data: dict) -> BatchUnameSuccessResponseItem:
    out: BatchUnameSuccessResponseItem = {}  # type: ignore[typeddict-item]
    if "uname" in data:
        out["uname"] = data["uname"]
    else:
        raise DeserializationError("BatchUnameSuccessResponseItem.uname required")
    if "username" in data:
        out["username"] = data["username"]
    else:
        raise DeserializationError("BatchUnameSuccessResponseItem.username required")
    return out
