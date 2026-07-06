"""Generated from Smithy shape ``com.amazonaws.connect#UserReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.user_id


class UserReference(TypedDict, closed=True):
    id: NotRequired["aws_sdk_connect.types.user_id.UserId"]
    """<p>The unique identifier for the user.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserReference) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> UserReference:
    out: UserReference = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
