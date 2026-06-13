"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#SemanticModality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation_runtime.errors import DeserializationError

"""Semantic modality enum"""
SemanticModality: TypeAlias = Literal[
    "DOCUMENT",
    "IMAGE",
    "AUDIO",
    "VIDEO",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOCUMENT",
        "IMAGE",
        "AUDIO",
        "VIDEO",
    )
)


def serialize_aws_json_1_1(value: SemanticModality) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SemanticModality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SemanticModality value: {data!r}")
    return cast(SemanticModality, data)
