"""Generated from Smithy shape ``com.amazonaws.kafka#ClusterType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of cluster.</p>"""
ClusterType: TypeAlias = Literal[
    "PROVISIONED",
    "SERVERLESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterType) -> str:
    return value


def deserialize_json(data: str) -> ClusterType:
    return cast(ClusterType, data)
