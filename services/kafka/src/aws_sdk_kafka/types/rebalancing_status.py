"""Generated from Smithy shape ``com.amazonaws.kafka#RebalancingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>Intelligent rebalancing status. The default intelligent rebalancing status is ACTIVE for all new Express-based clusters.</p>"""
RebalancingStatus: TypeAlias = Literal[
    "PAUSED",
    "ACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PAUSED",
        "ACTIVE",
    )
)


def serialize_json(value: RebalancingStatus) -> str:
    return value


def deserialize_json(data: str) -> RebalancingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RebalancingStatus value: {data!r}")
    return cast(RebalancingStatus, data)
