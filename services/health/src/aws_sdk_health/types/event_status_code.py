"""Generated from Smithy shape ``com.amazonaws.health#eventStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_health.errors import DeserializationError

eventStatusCode: TypeAlias = Literal[
    "open",
    "closed",
    "upcoming",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "open",
        "closed",
        "upcoming",
    )
)


def serialize_aws_json_1_1(value: eventStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> eventStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown eventStatusCode value: {data!r}")
    return cast(eventStatusCode, data)
