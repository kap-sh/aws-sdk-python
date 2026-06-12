"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

RuleStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: RuleStatus) -> str:
    return value


def deserialize_json(data: str) -> RuleStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleStatus value: {data!r}")
    return cast(RuleStatus, data)
