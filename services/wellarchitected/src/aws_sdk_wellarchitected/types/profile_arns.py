"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.profile_arn

ProfileArns: TypeAlias = list["aws_sdk_wellarchitected.types.profile_arn.ProfileArn"]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileArns) -> list:
    return list(value)


def deserialize_json(data: list) -> ProfileArns:
    return list(data)
