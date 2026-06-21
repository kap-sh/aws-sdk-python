"""Generated from Smithy shape ``com.amazonaws.translate#MergeStrategy``."""

from typing import Literal, TypeAlias, cast

MergeStrategy: TypeAlias = Literal["OVERWRITE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MergeStrategy:
    return cast(MergeStrategy, data)
