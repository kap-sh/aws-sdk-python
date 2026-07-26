"""Generated from Smithy shape ``com.amazonaws.codecommit#ReactionForComment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.count
    import capo_codecommit.types.reaction_users_list
    import capo_codecommit.types.reaction_value_formats


class ReactionForComment(TypedDict, closed=True):
    reaction: NotRequired[
        "capo_codecommit.types.reaction_value_formats.ReactionValueFormats"
    ]
    """<p>The reaction for a specified comment.</p>"""
    reaction_users: NotRequired[
        "capo_codecommit.types.reaction_users_list.ReactionUsersList"
    ]
    """<p>The Amazon Resource Names (ARNs) of users who have provided reactions to the comment.</p>"""
    reactions_from_deleted_users_count: NotRequired["capo_codecommit.types.count.Count"]
    """<p>A numerical count of users who reacted with the specified emoji whose identities have been subsequently deleted from IAM. While these IAM users or roles no longer exist, the reactions might still appear in total reaction counts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReactionForComment) -> dict:
    out: dict = {}
    if "reaction" in value:
        import capo_codecommit.types.reaction_value_formats

        out["reaction"] = (
            capo_codecommit.types.reaction_value_formats.serialize_aws_json_1_1(
                value["reaction"]
            )
        )
    if "reaction_users" in value:
        import capo_codecommit.types.reaction_users_list

        out["reactionUsers"] = (
            capo_codecommit.types.reaction_users_list.serialize_aws_json_1_1(
                value["reaction_users"]
            )
        )
    if "reactions_from_deleted_users_count" in value:
        out["reactionsFromDeletedUsersCount"] = value[
            "reactions_from_deleted_users_count"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReactionForComment:
    out: ReactionForComment = {}  # type: ignore[typeddict-item]
    if "reaction" in data:
        import capo_codecommit.types.reaction_value_formats

        out["reaction"] = (
            capo_codecommit.types.reaction_value_formats.deserialize_aws_json_1_1(
                data["reaction"]
            )
        )
    if "reactionUsers" in data:
        import capo_codecommit.types.reaction_users_list

        out["reaction_users"] = (
            capo_codecommit.types.reaction_users_list.deserialize_aws_json_1_1(
                data["reactionUsers"]
            )
        )
    if "reactionsFromDeletedUsersCount" in data:
        out["reactions_from_deleted_users_count"] = data[
            "reactionsFromDeletedUsersCount"
        ]
    return out
