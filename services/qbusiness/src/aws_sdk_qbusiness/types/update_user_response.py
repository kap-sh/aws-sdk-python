"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.user_aliases


class UpdateUserResponse(TypedDict, closed=True):
    user_aliases_added: NotRequired["aws_sdk_qbusiness.types.user_aliases.UserAliases"]
    """<p>The user aliases that have been to be added to a user id.</p>"""
    user_aliases_updated: NotRequired[
        "aws_sdk_qbusiness.types.user_aliases.UserAliases"
    ]
    """<p>The user aliases attached to a user id that have been updated.</p>"""
    user_aliases_deleted: NotRequired[
        "aws_sdk_qbusiness.types.user_aliases.UserAliases"
    ]
    """<p>The user aliases that have been deleted from a user id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserResponse) -> dict:
    out: dict = {}
    if "user_aliases_added" in value:
        import aws_sdk_qbusiness.types.user_aliases

        out["userAliasesAdded"] = aws_sdk_qbusiness.types.user_aliases.serialize_json(
            value["user_aliases_added"]
        )
    if "user_aliases_updated" in value:
        import aws_sdk_qbusiness.types.user_aliases

        out["userAliasesUpdated"] = aws_sdk_qbusiness.types.user_aliases.serialize_json(
            value["user_aliases_updated"]
        )
    if "user_aliases_deleted" in value:
        import aws_sdk_qbusiness.types.user_aliases

        out["userAliasesDeleted"] = aws_sdk_qbusiness.types.user_aliases.serialize_json(
            value["user_aliases_deleted"]
        )
    return out


def deserialize_json(data: dict) -> UpdateUserResponse:
    out: UpdateUserResponse = {}  # type: ignore[typeddict-item]
    if "userAliasesAdded" in data:
        import aws_sdk_qbusiness.types.user_aliases

        out["user_aliases_added"] = (
            aws_sdk_qbusiness.types.user_aliases.deserialize_json(
                data["userAliasesAdded"]
            )
        )
    if "userAliasesUpdated" in data:
        import aws_sdk_qbusiness.types.user_aliases

        out["user_aliases_updated"] = (
            aws_sdk_qbusiness.types.user_aliases.deserialize_json(
                data["userAliasesUpdated"]
            )
        )
    if "userAliasesDeleted" in data:
        import aws_sdk_qbusiness.types.user_aliases

        out["user_aliases_deleted"] = (
            aws_sdk_qbusiness.types.user_aliases.deserialize_json(
                data["userAliasesDeleted"]
            )
        )
    return out
