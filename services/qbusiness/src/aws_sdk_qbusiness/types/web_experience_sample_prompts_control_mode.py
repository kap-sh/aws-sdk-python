"""Generated from Smithy shape ``com.amazonaws.qbusiness#WebExperienceSamplePromptsControlMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

WebExperienceSamplePromptsControlMode: TypeAlias = Literal[
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


def serialize_json(value: WebExperienceSamplePromptsControlMode) -> str:
    return value


def deserialize_json(data: str) -> WebExperienceSamplePromptsControlMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WebExperienceSamplePromptsControlMode value: {data!r}"
        )
    return cast(WebExperienceSamplePromptsControlMode, data)
