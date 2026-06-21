"""Generated from Smithy shape ``com.amazonaws.rekognition#OrientationCorrection``."""

from typing import Literal, TypeAlias, cast

OrientationCorrection: TypeAlias = Literal[
    "ROTATE_0",
    "ROTATE_90",
    "ROTATE_180",
    "ROTATE_270",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrientationCorrection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrientationCorrection:
    return cast(OrientationCorrection, data)
