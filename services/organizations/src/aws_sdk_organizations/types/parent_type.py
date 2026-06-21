"""Generated from Smithy shape ``com.amazonaws.organizations#ParentType``."""

from typing import Literal, TypeAlias, cast

ParentType: TypeAlias = Literal[
    "ROOT",
    "ORGANIZATIONAL_UNIT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParentType:
    return cast(ParentType, data)
