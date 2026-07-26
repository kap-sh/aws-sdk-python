"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicationTopicNameConfigurationType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of replicated topic name.</p>"""
ReplicationTopicNameConfigurationType: TypeAlias = Literal[
    "PREFIXED_WITH_SOURCE_CLUSTER_ALIAS",
    "IDENTICAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationTopicNameConfigurationType) -> str:
    return value


def deserialize_json(data: str) -> ReplicationTopicNameConfigurationType:
    return cast(ReplicationTopicNameConfigurationType, data)
