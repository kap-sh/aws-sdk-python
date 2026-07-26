"""Generated from Smithy shape ``com.amazonaws.kendra#RelevanceType``."""

from typing import Literal, TypeAlias, cast

RelevanceType: TypeAlias = Literal[
    "RELEVANT",
    "NOT_RELEVANT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelevanceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RelevanceType:
    return cast(RelevanceType, data)
