"""Generated from Smithy shape ``com.amazonaws.resiliencehub#TestRisk``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

TestRisk: TypeAlias = Literal[
    "Small",
    "Medium",
    "High",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Small",
        "Medium",
        "High",
    )
)


def serialize_json(value: TestRisk) -> str:
    return value


def deserialize_json(data: str) -> TestRisk:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestRisk value: {data!r}")
    return cast(TestRisk, data)
