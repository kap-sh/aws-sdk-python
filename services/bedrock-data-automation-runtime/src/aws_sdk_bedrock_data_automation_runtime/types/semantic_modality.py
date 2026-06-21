"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#SemanticModality``."""

from typing import Literal, TypeAlias, cast

"""Semantic modality enum"""
SemanticModality: TypeAlias = Literal[
    "DOCUMENT",
    "IMAGE",
    "AUDIO",
    "VIDEO",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SemanticModality) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SemanticModality:
    return cast(SemanticModality, data)
