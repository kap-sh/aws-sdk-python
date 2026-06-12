"""Generated from Smithy shape ``com.amazonaws.acm#ValidationMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm.errors import DeserializationError

ValidationMethod: TypeAlias = Literal[
    "EMAIL",
    "DNS",
    "HTTP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMAIL",
        "DNS",
        "HTTP",
    )
)


def serialize_aws_json_1_1(value: ValidationMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValidationMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationMethod value: {data!r}")
    return cast(ValidationMethod, data)
