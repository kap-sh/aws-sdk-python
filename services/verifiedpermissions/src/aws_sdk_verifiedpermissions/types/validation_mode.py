"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ValidationMode``."""

from typing import Literal, TypeAlias, cast

ValidationMode: TypeAlias = Literal[
    "OFF",
    "STRICT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationMode:
    return cast(ValidationMode, data)
