"""Generated from Smithy shape ``com.amazonaws.kendra#KeyLocation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

KeyLocation: TypeAlias = Literal[
    "URL",
    "SECRET_MANAGER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "URL",
        "SECRET_MANAGER",
    )
)


def serialize_aws_json_1_1(value: KeyLocation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyLocation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyLocation value: {data!r}")
    return cast(KeyLocation, data)
