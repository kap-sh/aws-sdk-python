"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ModelQuality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

ModelQuality: TypeAlias = Literal[
    "QUALITY_THRESHOLD_MET",
    "CANNOT_DETERMINE_QUALITY",
    "POOR_QUALITY_DETECTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUALITY_THRESHOLD_MET",
        "CANNOT_DETERMINE_QUALITY",
        "POOR_QUALITY_DETECTED",
    )
)


def serialize_aws_json_1_0(value: ModelQuality) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ModelQuality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelQuality value: {data!r}")
    return cast(ModelQuality, data)
