"""Generated from Smithy shape ``com.amazonaws.qbusiness#ResponseScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

ResponseScope: TypeAlias = Literal[
    "ENTERPRISE_CONTENT_ONLY",
    "EXTENDED_KNOWLEDGE_ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENTERPRISE_CONTENT_ONLY",
        "EXTENDED_KNOWLEDGE_ENABLED",
    )
)


def serialize_json(value: ResponseScope) -> str:
    return value


def deserialize_json(data: str) -> ResponseScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResponseScope value: {data!r}")
    return cast(ResponseScope, data)
