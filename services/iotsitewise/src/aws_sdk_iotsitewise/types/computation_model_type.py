"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

ComputationModelType: TypeAlias = Literal["ANOMALY_DETECTION",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ANOMALY_DETECTION",))


def serialize_json(value: ComputationModelType) -> str:
    return value


def deserialize_json(data: str) -> ComputationModelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputationModelType value: {data!r}")
    return cast(ComputationModelType, data)
