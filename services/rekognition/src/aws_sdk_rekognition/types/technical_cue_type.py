"""Generated from Smithy shape ``com.amazonaws.rekognition#TechnicalCueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

TechnicalCueType: TypeAlias = Literal[
    "ColorBars",
    "EndCredits",
    "BlackFrames",
    "OpeningCredits",
    "StudioLogo",
    "Slate",
    "Content",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ColorBars",
        "EndCredits",
        "BlackFrames",
        "OpeningCredits",
        "StudioLogo",
        "Slate",
        "Content",
    )
)


def serialize_aws_json_1_1(value: TechnicalCueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TechnicalCueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TechnicalCueType value: {data!r}")
    return cast(TechnicalCueType, data)
