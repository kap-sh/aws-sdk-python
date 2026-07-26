"""Generated from Smithy shape ``com.amazonaws.rekognition#TechnicalCueType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: TechnicalCueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TechnicalCueType:
    return cast(TechnicalCueType, data)
