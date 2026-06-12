"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ImageStandardGenerativeFieldType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

ImageStandardGenerativeFieldType: TypeAlias = Literal[
    "IMAGE_SUMMARY",
    "IAB",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IMAGE_SUMMARY",
        "IAB",
    )
)


def serialize_json(value: ImageStandardGenerativeFieldType) -> str:
    return value


def deserialize_json(data: str) -> ImageStandardGenerativeFieldType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ImageStandardGenerativeFieldType value: {data!r}"
        )
    return cast(ImageStandardGenerativeFieldType, data)
