"""Generated from Smithy shape ``com.amazonaws.securityhub#RuleStatusV2``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

RuleStatusV2: TypeAlias = Literal[
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


def serialize_json(value: RuleStatusV2) -> str:
    return value


def deserialize_json(data: str) -> RuleStatusV2:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleStatusV2 value: {data!r}")
    return cast(RuleStatusV2, data)
