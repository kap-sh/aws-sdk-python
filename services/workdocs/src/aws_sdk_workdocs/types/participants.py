"""Generated from Smithy shape ``com.amazonaws.workdocs#Participants``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.group_metadata_list
    import aws_sdk_workdocs.types.user_metadata_list


class Participants(TypedDict):
    users: NotRequired["aws_sdk_workdocs.types.user_metadata_list.UserMetadataList"]
    """<p>The list of users.</p>"""
    groups: NotRequired["aws_sdk_workdocs.types.group_metadata_list.GroupMetadataList"]
    """<p>The list of user groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Participants) -> dict:
    out: dict = {}
    if "users" in value:
        import aws_sdk_workdocs.types.user_metadata_list

        out["Users"] = aws_sdk_workdocs.types.user_metadata_list.serialize_json(
            value["users"]
        )
    if "groups" in value:
        import aws_sdk_workdocs.types.group_metadata_list

        out["Groups"] = aws_sdk_workdocs.types.group_metadata_list.serialize_json(
            value["groups"]
        )
    return out


def deserialize_json(data: dict) -> Participants:
    out: Participants = {}  # type: ignore[typeddict-item]
    if "Users" in data:
        import aws_sdk_workdocs.types.user_metadata_list

        out["users"] = aws_sdk_workdocs.types.user_metadata_list.deserialize_json(
            data["Users"]
        )
    if "Groups" in data:
        import aws_sdk_workdocs.types.group_metadata_list

        out["groups"] = aws_sdk_workdocs.types.group_metadata_list.deserialize_json(
            data["Groups"]
        )
    return out
