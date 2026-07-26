"""Generated from Smithy shape ``com.amazonaws.kendra#MissingAttributeKeyStrategy``."""

from typing import Literal, TypeAlias, cast

MissingAttributeKeyStrategy: TypeAlias = Literal[
    "IGNORE",
    "COLLAPSE",
    "EXPAND",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MissingAttributeKeyStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MissingAttributeKeyStrategy:
    return cast(MissingAttributeKeyStrategy, data)
