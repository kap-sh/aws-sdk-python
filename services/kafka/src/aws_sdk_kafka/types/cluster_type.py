"""Generated from Smithy shape ``com.amazonaws.kafka#ClusterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>The type of cluster.</p>"""
ClusterType: TypeAlias = Literal[
    "PROVISIONED",
    "SERVERLESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONED",
        "SERVERLESS",
    )
)


def serialize_json(value: ClusterType) -> str:
    return value


def deserialize_json(data: str) -> ClusterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterType value: {data!r}")
    return cast(ClusterType, data)
