"""Generated from Smithy shape ``com.amazonaws.codecommit#MergeOptionTypeEnum``."""

from typing import Literal, TypeAlias, cast

MergeOptionTypeEnum: TypeAlias = Literal[
    "FAST_FORWARD_MERGE",
    "SQUASH_MERGE",
    "THREE_WAY_MERGE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeOptionTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MergeOptionTypeEnum:
    return cast(MergeOptionTypeEnum, data)
