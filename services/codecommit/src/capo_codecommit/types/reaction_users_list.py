"""Generated from Smithy shape ``com.amazonaws.codecommit#ReactionUsersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecommit.types.arn

ReactionUsersList: TypeAlias = list["capo_codecommit.types.arn.Arn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReactionUsersList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ReactionUsersList:
    return list(data)
