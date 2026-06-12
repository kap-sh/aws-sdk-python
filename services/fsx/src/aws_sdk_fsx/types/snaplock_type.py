"""Generated from Smithy shape ``com.amazonaws.fsx#SnaplockType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

SnaplockType: TypeAlias = Literal[
    "COMPLIANCE",
    "ENTERPRISE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLIANCE",
        "ENTERPRISE",
    )
)


def serialize_aws_json_1_1(value: SnaplockType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SnaplockType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnaplockType value: {data!r}")
    return cast(SnaplockType, data)
