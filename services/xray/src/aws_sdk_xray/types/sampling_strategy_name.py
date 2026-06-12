"""Generated from Smithy shape ``com.amazonaws.xray#SamplingStrategyName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_xray.errors import DeserializationError

SamplingStrategyName: TypeAlias = Literal[
    "PartialScan",
    "FixedRate",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PartialScan",
        "FixedRate",
    )
)


def serialize_json(value: SamplingStrategyName) -> str:
    return value


def deserialize_json(data: str) -> SamplingStrategyName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SamplingStrategyName value: {data!r}")
    return cast(SamplingStrategyName, data)
