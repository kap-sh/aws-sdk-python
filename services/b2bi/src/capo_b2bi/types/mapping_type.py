"""Generated from Smithy shape ``com.amazonaws.b2bi#MappingType``."""

from typing import Literal, TypeAlias, cast

MappingType: TypeAlias = Literal[
    "JSONATA",
    "XSLT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MappingType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MappingType:
    return cast(MappingType, data)
