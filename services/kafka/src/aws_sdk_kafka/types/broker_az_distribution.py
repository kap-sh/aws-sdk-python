"""Generated from Smithy shape ``com.amazonaws.kafka#BrokerAZDistribution``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>The distribution of broker nodes across Availability Zones. This is an optional parameter. If you don't specify it, Amazon MSK gives it the value DEFAULT. You can also explicitly set this parameter to the value DEFAULT. No other values are currently allowed.</p> <p>Amazon MSK distributes the broker nodes evenly across the Availability Zones that correspond to the subnets you provide when you create the cluster.</p>"""
BrokerAZDistribution: TypeAlias = Literal["DEFAULT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DEFAULT",))


def serialize_json(value: BrokerAZDistribution) -> str:
    return value


def deserialize_json(data: str) -> BrokerAZDistribution:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BrokerAZDistribution value: {data!r}")
    return cast(BrokerAZDistribution, data)
