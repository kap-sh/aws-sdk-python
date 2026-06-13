"""Generated from Smithy shape ``com.amazonaws.bedrock#ApplicationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

ApplicationType: TypeAlias = Literal[
    "ModelEvaluation",
    "RagEvaluation",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ModelEvaluation",
        "RagEvaluation",
    )
)


def serialize_json(value: ApplicationType) -> str:
    return value


def deserialize_json(data: str) -> ApplicationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationType value: {data!r}")
    return cast(ApplicationType, data)
