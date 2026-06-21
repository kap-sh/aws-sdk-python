"""Generated from Smithy shape ``com.amazonaws.b2bi#ConversionSourceFormat``."""

from typing import Literal, TypeAlias, cast

ConversionSourceFormat: TypeAlias = Literal[
    "JSON",
    "XML",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConversionSourceFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConversionSourceFormat:
    return cast(ConversionSourceFormat, data)
