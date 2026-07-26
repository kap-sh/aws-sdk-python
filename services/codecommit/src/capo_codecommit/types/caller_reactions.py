"""Generated from Smithy shape ``com.amazonaws.codecommit#CallerReactions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.reaction_value

CallerReactions: TypeAlias = list["capo_codecommit.types.reaction_value.ReactionValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CallerReactions) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CallerReactions:
    return list(data)
