"""Generated from Smithy shape ``com.amazonaws.wickr#BatchUserSuccessResponseItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.user_id


class BatchUserSuccessResponseItem(TypedDict, closed=True):
    user_id: "aws_sdk_wickr.types.user_id.UserId"
    """<p>The user ID that was successfully processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUserSuccessResponseItem) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> BatchUserSuccessResponseItem:
    out: BatchUserSuccessResponseItem = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("BatchUserSuccessResponseItem.user_id required")
    return out
