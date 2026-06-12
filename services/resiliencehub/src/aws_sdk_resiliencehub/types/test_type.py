"""Generated from Smithy shape ``com.amazonaws.resiliencehub#TestType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

TestType: TypeAlias = Literal[
    "Software",
    "Hardware",
    "AZ",
    "Region",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Software",
        "Hardware",
        "AZ",
        "Region",
    )
)


def serialize_json(value: TestType) -> str:
    return value


def deserialize_json(data: str) -> TestType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestType value: {data!r}")
    return cast(TestType, data)
