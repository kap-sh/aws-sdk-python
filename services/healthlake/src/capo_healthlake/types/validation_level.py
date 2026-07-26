"""Generated from Smithy shape ``com.amazonaws.healthlake#ValidationLevel``."""

from typing import Literal, TypeAlias, cast

ValidationLevel: TypeAlias = Literal[
    "strict",
    "structure-only",
    "minimal",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationLevel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationLevel:
    return cast(ValidationLevel, data)
