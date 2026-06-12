"""Generated from Smithy shape ``com.amazonaws.wellarchitected#MetricType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

MetricType: TypeAlias = Literal["WORKLOAD",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("WORKLOAD",))


def serialize_json(value: MetricType) -> str:
    return value


def deserialize_json(data: str) -> MetricType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricType value: {data!r}")
    return cast(MetricType, data)
