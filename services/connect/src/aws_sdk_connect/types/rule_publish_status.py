"""Generated from Smithy shape ``com.amazonaws.connect#RulePublishStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

RulePublishStatus: TypeAlias = Literal[
    "DRAFT",
    "PUBLISHED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DRAFT",
        "PUBLISHED",
    )
)


def serialize_json(value: RulePublishStatus) -> str:
    return value


def deserialize_json(data: str) -> RulePublishStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RulePublishStatus value: {data!r}")
    return cast(RulePublishStatus, data)
