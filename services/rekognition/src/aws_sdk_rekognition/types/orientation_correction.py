"""Generated from Smithy shape ``com.amazonaws.rekognition#OrientationCorrection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

OrientationCorrection: TypeAlias = Literal[
    "ROTATE_0",
    "ROTATE_90",
    "ROTATE_180",
    "ROTATE_270",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROTATE_0",
        "ROTATE_90",
        "ROTATE_180",
        "ROTATE_270",
    )
)


def serialize_aws_json_1_1(value: OrientationCorrection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrientationCorrection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OrientationCorrection value: {data!r}")
    return cast(OrientationCorrection, data)
