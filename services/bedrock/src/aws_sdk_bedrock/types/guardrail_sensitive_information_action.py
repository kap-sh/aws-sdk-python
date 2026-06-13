"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailSensitiveInformationAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

GuardrailSensitiveInformationAction: TypeAlias = Literal[
    "BLOCK",
    "ANONYMIZE",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLOCK",
        "ANONYMIZE",
        "NONE",
    )
)


def serialize_json(value: GuardrailSensitiveInformationAction) -> str:
    return value


def deserialize_json(data: str) -> GuardrailSensitiveInformationAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GuardrailSensitiveInformationAction value: {data!r}"
        )
    return cast(GuardrailSensitiveInformationAction, data)
