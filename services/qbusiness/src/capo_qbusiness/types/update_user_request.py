"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.string
    import capo_qbusiness.types.user_aliases


class UpdateUserRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the application the user is attached to.</p>"""
    user_id: "capo_qbusiness.types.string.String"
    """<p>The email id attached to the user.</p>"""
    user_aliases_to_update: NotRequired["capo_qbusiness.types.user_aliases.UserAliases"]
    """<p>The user aliases attached to the user id that are to be updated.</p>"""
    user_aliases_to_delete: NotRequired["capo_qbusiness.types.user_aliases.UserAliases"]
    """<p>The user aliases attached to the user id that are to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserRequest) -> dict:
    out: dict = {}
    if "user_aliases_to_update" in value:
        import capo_qbusiness.types.user_aliases

        out["userAliasesToUpdate"] = capo_qbusiness.types.user_aliases.serialize_json(
            value["user_aliases_to_update"]
        )
    if "user_aliases_to_delete" in value:
        import capo_qbusiness.types.user_aliases

        out["userAliasesToDelete"] = capo_qbusiness.types.user_aliases.serialize_json(
            value["user_aliases_to_delete"]
        )
    return out


def deserialize_json(data: dict) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    if "userAliasesToUpdate" in data:
        import capo_qbusiness.types.user_aliases

        out["user_aliases_to_update"] = (
            capo_qbusiness.types.user_aliases.deserialize_json(
                data["userAliasesToUpdate"]
            )
        )
    if "userAliasesToDelete" in data:
        import capo_qbusiness.types.user_aliases

        out["user_aliases_to_delete"] = (
            capo_qbusiness.types.user_aliases.deserialize_json(
                data["userAliasesToDelete"]
            )
        )
    return out
