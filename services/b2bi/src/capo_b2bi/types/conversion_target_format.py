"""Generated from Smithy shape ``com.amazonaws.b2bi#ConversionTargetFormat``."""

from typing import Literal, TypeAlias, cast

ConversionTargetFormat: TypeAlias = Literal["X12",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConversionTargetFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConversionTargetFormat:
    return cast(ConversionTargetFormat, data)
