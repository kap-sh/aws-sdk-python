"""Generated from Smithy shape ``com.amazonaws.pi#FineGrainedAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pi.errors import DeserializationError

FineGrainedAction: TypeAlias = Literal[
    "DescribeDimensionKeys",
    "GetDimensionKeyDetails",
    "GetResourceMetrics",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DescribeDimensionKeys",
        "GetDimensionKeyDetails",
        "GetResourceMetrics",
    )
)


def serialize_aws_json_1_1(value: FineGrainedAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FineGrainedAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FineGrainedAction value: {data!r}")
    return cast(FineGrainedAction, data)
