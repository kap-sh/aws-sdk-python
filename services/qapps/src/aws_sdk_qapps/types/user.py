"""Generated from Smithy shape ``com.amazonaws.qapps#User``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qapps.types.user_id


class User(TypedDict):
    user_id: NotRequired["aws_sdk_qapps.types.user_id.UserId"]
    """<p>The unique identifier of a user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: User) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    return out
