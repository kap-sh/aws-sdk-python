"""Generated from Smithy shape ``com.amazonaws.mq#SanitizationWarningReason``."""

from typing import Literal, TypeAlias, cast

"""<p>The reason for which the configuration elements or attributes were sanitized.</p>"""
SanitizationWarningReason: TypeAlias = Literal[
    "DISALLOWED_ELEMENT_REMOVED",
    "DISALLOWED_ATTRIBUTE_REMOVED",
    "INVALID_ATTRIBUTE_VALUE_REMOVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SanitizationWarningReason) -> str:
    return value


def deserialize_json(data: str) -> SanitizationWarningReason:
    return cast(SanitizationWarningReason, data)
