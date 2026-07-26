"""Generated from Smithy shape ``com.amazonaws.codecommit#ReactionsForCommentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.reaction_for_comment

ReactionsForCommentList: TypeAlias = list[
    "capo_codecommit.types.reaction_for_comment.ReactionForComment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReactionsForCommentList) -> list:
    import capo_codecommit.types.reaction_for_comment

    out: list = []
    for item in value:
        out.append(
            capo_codecommit.types.reaction_for_comment.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReactionsForCommentList:
    import capo_codecommit.types.reaction_for_comment

    out: ReactionsForCommentList = []
    for item in data:
        out.append(
            capo_codecommit.types.reaction_for_comment.deserialize_aws_json_1_1(item)
        )
    return out
