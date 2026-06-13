"""Generated from Smithy shape ``com.amazonaws.qbusiness#RuleType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

RuleType: TypeAlias = Literal[
    "CONTENT_BLOCKER_RULE",
    "CONTENT_RETRIEVAL_RULE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTENT_BLOCKER_RULE",
        "CONTENT_RETRIEVAL_RULE",
    )
)


def serialize_json(value: RuleType) -> str:
    return value


def deserialize_json(data: str) -> RuleType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleType value: {data!r}")
    return cast(RuleType, data)
