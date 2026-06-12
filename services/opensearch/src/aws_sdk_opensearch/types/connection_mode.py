"""Generated from Smithy shape ``com.amazonaws.opensearch#ConnectionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The connection mode for the cross-cluster connection.</p> <ul> <li> <p> <b>DIRECT</b> - Used for cross-cluster search or cross-cluster replication.</p> </li> <li> <p> <b>VPC_ENDPOINT</b> - Used for remote reindex between Amazon OpenSearch Service VPC domains.</p> </li> </ul>"""
ConnectionMode: TypeAlias = Literal[
    "DIRECT",
    "VPC_ENDPOINT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIRECT",
        "VPC_ENDPOINT",
    )
)


def serialize_json(value: ConnectionMode) -> str:
    return value


def deserialize_json(data: str) -> ConnectionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionMode value: {data!r}")
    return cast(ConnectionMode, data)
