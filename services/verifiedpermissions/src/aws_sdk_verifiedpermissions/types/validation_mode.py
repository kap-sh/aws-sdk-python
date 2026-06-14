"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ValidationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_verifiedpermissions.errors import DeserializationError

ValidationMode: TypeAlias = Literal[
    "OFF",
    "STRICT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "STRICT",
    )
)


def serialize_aws_json_1_0(value: ValidationMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationMode value: {data!r}")
    return cast(ValidationMode, data)
