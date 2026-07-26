"""Generated from Smithy shape ``com.amazonaws.gamelift#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.non_zero_and_max_string

StringList: TypeAlias = list[
    "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> StringList:
    return list(data)
