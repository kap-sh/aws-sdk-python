"""Generated from Smithy shape ``com.amazonaws.connect#CreateUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.user_id


class CreateUserResponse(TypedDict, closed=True):
    user_id: NotRequired["aws_sdk_connect.types.user_id.UserId"]
    """<p>The identifier of the user account.</p>"""
    user_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the user account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserResponse) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "user_arn" in value:
        out["UserArn"] = value["user_arn"]
    return out


def deserialize_json(data: dict) -> CreateUserResponse:
    out: CreateUserResponse = {}  # type: ignore[typeddict-item]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    if "UserArn" in data:
        out["user_arn"] = data["UserArn"]
    return out
