"""Generated from Smithy shape ``com.amazonaws.b2bi#FromFormat``."""

from typing import Literal, TypeAlias, cast

FromFormat: TypeAlias = Literal["X12",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FromFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FromFormat:
    return cast(FromFormat, data)
