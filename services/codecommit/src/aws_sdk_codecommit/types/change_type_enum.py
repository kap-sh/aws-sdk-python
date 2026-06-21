"""Generated from Smithy shape ``com.amazonaws.codecommit#ChangeTypeEnum``."""

from typing import Literal, TypeAlias, cast

ChangeTypeEnum: TypeAlias = Literal[
    "A",
    "M",
    "D",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChangeTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChangeTypeEnum:
    return cast(ChangeTypeEnum, data)
