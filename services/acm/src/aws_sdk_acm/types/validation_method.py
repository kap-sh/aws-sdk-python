"""Generated from Smithy shape ``com.amazonaws.acm#ValidationMethod``."""

from typing import Literal, TypeAlias, cast

ValidationMethod: TypeAlias = Literal[
    "EMAIL",
    "DNS",
    "HTTP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValidationMethod:
    return cast(ValidationMethod, data)
