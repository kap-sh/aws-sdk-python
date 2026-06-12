"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseEntryPointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

TestCaseEntryPointType: TypeAlias = Literal[
    "VOICE_CALL",
    "CHAT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VOICE_CALL",
        "CHAT",
    )
)


def serialize_json(value: TestCaseEntryPointType) -> str:
    return value


def deserialize_json(data: str) -> TestCaseEntryPointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestCaseEntryPointType value: {data!r}")
    return cast(TestCaseEntryPointType, data)
