"""Generated from Smithy shape ``com.amazonaws.rekognition#CustomizationFeature``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

CustomizationFeature: TypeAlias = Literal[
    "CONTENT_MODERATION",
    "CUSTOM_LABELS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTENT_MODERATION",
        "CUSTOM_LABELS",
    )
)


def serialize_aws_json_1_1(value: CustomizationFeature) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomizationFeature:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomizationFeature value: {data!r}")
    return cast(CustomizationFeature, data)
