"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerCommandStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.non_zero_and255_max_string

ContainerCommandStringList: TypeAlias = list[
    "aws_sdk_gamelift.types.non_zero_and255_max_string.NonZeroAnd255MaxString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerCommandStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ContainerCommandStringList:
    return list(data)
