"""Generated from Smithy shape ``com.amazonaws.amplify#JobType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplify.errors import DeserializationError

JobType: TypeAlias = Literal[
    "RELEASE",
    "RETRY",
    "MANUAL",
    "WEB_HOOK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RELEASE",
        "RETRY",
        "MANUAL",
        "WEB_HOOK",
    )
)


def serialize_json(value: JobType) -> str:
    return value


def deserialize_json(data: str) -> JobType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobType value: {data!r}")
    return cast(JobType, data)
