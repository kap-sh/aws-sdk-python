"""Generated from Smithy shape ``com.amazonaws.codeconnections#BlockerType``."""

from typing import Literal, TypeAlias, cast

BlockerType: TypeAlias = Literal["AUTOMATED",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BlockerType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BlockerType:
    return cast(BlockerType, data)
