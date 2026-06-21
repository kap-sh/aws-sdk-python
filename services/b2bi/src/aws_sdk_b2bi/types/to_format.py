"""Generated from Smithy shape ``com.amazonaws.b2bi#ToFormat``."""

from typing import Literal, TypeAlias, cast

ToFormat: TypeAlias = Literal["X12",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ToFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ToFormat:
    return cast(ToFormat, data)
