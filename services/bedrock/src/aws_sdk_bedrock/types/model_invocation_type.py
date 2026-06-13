"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelInvocationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

ModelInvocationType: TypeAlias = Literal[
    "InvokeModel",
    "Converse",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InvokeModel",
        "Converse",
    )
)


def serialize_json(value: ModelInvocationType) -> str:
    return value


def deserialize_json(data: str) -> ModelInvocationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelInvocationType value: {data!r}")
    return cast(ModelInvocationType, data)
