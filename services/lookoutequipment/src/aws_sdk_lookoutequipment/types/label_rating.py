"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#LabelRating``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

LabelRating: TypeAlias = Literal[
    "ANOMALY",
    "NO_ANOMALY",
    "NEUTRAL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ANOMALY",
        "NO_ANOMALY",
        "NEUTRAL",
    )
)


def serialize_aws_json_1_0(value: LabelRating) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LabelRating:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LabelRating value: {data!r}")
    return cast(LabelRating, data)
