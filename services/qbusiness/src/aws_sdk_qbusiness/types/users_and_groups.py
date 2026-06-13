"""Generated from Smithy shape ``com.amazonaws.qbusiness#UsersAndGroups``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.user_groups
    import aws_sdk_qbusiness.types.user_ids


class UsersAndGroups(TypedDict):
    user_ids: NotRequired["aws_sdk_qbusiness.types.user_ids.UserIds"]
    """<p>The user ids associated with a topic control rule.</p>"""
    user_groups: NotRequired["aws_sdk_qbusiness.types.user_groups.UserGroups"]
    """<p>The user group names associated with a topic control rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsersAndGroups) -> dict:
    out: dict = {}
    if "user_ids" in value:
        import aws_sdk_qbusiness.types.user_ids

        out["userIds"] = aws_sdk_qbusiness.types.user_ids.serialize_json(
            value["user_ids"]
        )
    if "user_groups" in value:
        import aws_sdk_qbusiness.types.user_groups

        out["userGroups"] = aws_sdk_qbusiness.types.user_groups.serialize_json(
            value["user_groups"]
        )
    return out


def deserialize_json(data: dict) -> UsersAndGroups:
    out: UsersAndGroups = {}  # type: ignore[typeddict-item]
    if "userIds" in data:
        import aws_sdk_qbusiness.types.user_ids

        out["user_ids"] = aws_sdk_qbusiness.types.user_ids.deserialize_json(
            data["userIds"]
        )
    if "userGroups" in data:
        import aws_sdk_qbusiness.types.user_groups

        out["user_groups"] = aws_sdk_qbusiness.types.user_groups.deserialize_json(
            data["userGroups"]
        )
    return out
