"""Generated from Smithy shape ``com.amazonaws.mq#SanitizationWarningReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mq.errors import DeserializationError

"""<p>The reason for which the configuration elements or attributes were sanitized.</p>"""
SanitizationWarningReason: TypeAlias = Literal[
    "DISALLOWED_ELEMENT_REMOVED",
    "DISALLOWED_ATTRIBUTE_REMOVED",
    "INVALID_ATTRIBUTE_VALUE_REMOVED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISALLOWED_ELEMENT_REMOVED",
        "DISALLOWED_ATTRIBUTE_REMOVED",
        "INVALID_ATTRIBUTE_VALUE_REMOVED",
    )
)


def serialize_json(value: SanitizationWarningReason) -> str:
    return value


def deserialize_json(data: str) -> SanitizationWarningReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SanitizationWarningReason value: {data!r}")
    return cast(SanitizationWarningReason, data)
