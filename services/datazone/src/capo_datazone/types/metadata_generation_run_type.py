"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataGenerationRunType``."""

from typing import Literal, TypeAlias, cast

MetadataGenerationRunType: TypeAlias = Literal[
    "BUSINESS_DESCRIPTIONS",
    "BUSINESS_NAMES",
    "BUSINESS_GLOSSARY_ASSOCIATIONS",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataGenerationRunType) -> str:
    return value


def deserialize_json(data: str) -> MetadataGenerationRunType:
    return cast(MetadataGenerationRunType, data)
