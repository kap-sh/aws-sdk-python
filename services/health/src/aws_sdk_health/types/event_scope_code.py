"""Generated from Smithy shape ``com.amazonaws.health#eventScopeCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_health.errors import DeserializationError

eventScopeCode: TypeAlias = Literal[
    "PUBLIC",
    "ACCOUNT_SPECIFIC",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC",
        "ACCOUNT_SPECIFIC",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: eventScopeCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> eventScopeCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown eventScopeCode value: {data!r}")
    return cast(eventScopeCode, data)
