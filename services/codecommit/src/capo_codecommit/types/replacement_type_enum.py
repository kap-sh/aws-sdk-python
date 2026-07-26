"""Generated from Smithy shape ``com.amazonaws.codecommit#ReplacementTypeEnum``."""

from typing import Literal, TypeAlias, cast

ReplacementTypeEnum: TypeAlias = Literal[
    "KEEP_BASE",
    "KEEP_SOURCE",
    "KEEP_DESTINATION",
    "USE_NEW_CONTENT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplacementTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplacementTypeEnum:
    return cast(ReplacementTypeEnum, data)
