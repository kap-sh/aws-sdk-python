"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataGenerationRunType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

MetadataGenerationRunType: TypeAlias = Literal[
    "BUSINESS_DESCRIPTIONS",
    "BUSINESS_NAMES",
    "BUSINESS_GLOSSARY_ASSOCIATIONS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BUSINESS_DESCRIPTIONS",
        "BUSINESS_NAMES",
        "BUSINESS_GLOSSARY_ASSOCIATIONS",
    )
)


def serialize_json(value: MetadataGenerationRunType) -> str:
    return value


def deserialize_json(data: str) -> MetadataGenerationRunType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetadataGenerationRunType value: {data!r}")
    return cast(MetadataGenerationRunType, data)
