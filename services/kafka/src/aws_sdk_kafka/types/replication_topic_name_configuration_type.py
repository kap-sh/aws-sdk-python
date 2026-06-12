"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicationTopicNameConfigurationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>The type of replicated topic name.</p>"""
ReplicationTopicNameConfigurationType: TypeAlias = Literal[
    "PREFIXED_WITH_SOURCE_CLUSTER_ALIAS",
    "IDENTICAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PREFIXED_WITH_SOURCE_CLUSTER_ALIAS",
        "IDENTICAL",
    )
)


def serialize_json(value: ReplicationTopicNameConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> ReplicationTopicNameConfigurationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReplicationTopicNameConfigurationType value: {data!r}"
        )
    return cast(ReplicationTopicNameConfigurationType, data)
