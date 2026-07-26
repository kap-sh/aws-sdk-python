"""Generated from Smithy shape ``com.amazonaws.qbusiness#UsersAndGroups``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.user_groups
    import capo_qbusiness.types.user_ids


class UsersAndGroups(TypedDict, closed=True):
    user_ids: NotRequired["capo_qbusiness.types.user_ids.UserIds"]
    """<p>The user ids associated with a topic control rule.</p>"""
    user_groups: NotRequired["capo_qbusiness.types.user_groups.UserGroups"]
    """<p>The user group names associated with a topic control rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsersAndGroups) -> dict:
    out: dict = {}
    if "user_ids" in value:
        import capo_qbusiness.types.user_ids

        out["userIds"] = capo_qbusiness.types.user_ids.serialize_json(value["user_ids"])
    if "user_groups" in value:
        import capo_qbusiness.types.user_groups

        out["userGroups"] = capo_qbusiness.types.user_groups.serialize_json(
            value["user_groups"]
        )
    return out


def deserialize_json(data: dict) -> UsersAndGroups:
    out: UsersAndGroups = {}  # type: ignore[typeddict-item]
    if "userIds" in data:
        import capo_qbusiness.types.user_ids

        out["user_ids"] = capo_qbusiness.types.user_ids.deserialize_json(
            data["userIds"]
        )
    if "userGroups" in data:
        import capo_qbusiness.types.user_groups

        out["user_groups"] = capo_qbusiness.types.user_groups.deserialize_json(
            data["userGroups"]
        )
    return out
