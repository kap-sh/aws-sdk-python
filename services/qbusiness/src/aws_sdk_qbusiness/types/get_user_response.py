"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.user_aliases


class GetUserResponse(TypedDict, closed=True):
    user_aliases: NotRequired["aws_sdk_qbusiness.types.user_aliases.UserAliases"]
    """<p>A list of user aliases attached to a user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserResponse) -> dict:
    out: dict = {}
    if "user_aliases" in value:
        import aws_sdk_qbusiness.types.user_aliases

        out["userAliases"] = aws_sdk_qbusiness.types.user_aliases.serialize_json(
            value["user_aliases"]
        )
    return out


def deserialize_json(data: dict) -> GetUserResponse:
    out: GetUserResponse = {}  # type: ignore[typeddict-item]
    if "userAliases" in data:
        import aws_sdk_qbusiness.types.user_aliases

        out["user_aliases"] = aws_sdk_qbusiness.types.user_aliases.deserialize_json(
            data["userAliases"]
        )
    return out
