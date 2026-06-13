"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailOrigin``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

GuardrailOrigin: TypeAlias = Literal[
    "REQUEST",
    "ACCOUNT_ENFORCED",
    "ORGANIZATION_ENFORCED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUEST",
        "ACCOUNT_ENFORCED",
        "ORGANIZATION_ENFORCED",
    )
)


def serialize_json(value: GuardrailOrigin) -> str:
    return value


def deserialize_json(data: str) -> GuardrailOrigin:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailOrigin value: {data!r}")
    return cast(GuardrailOrigin, data)
