"""Generated from Smithy shape ``com.amazonaws.mq#DataReplicationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mq.errors import DeserializationError

"""<p>Specifies whether a broker is a part of a data replication pair.</p>"""
DataReplicationMode: TypeAlias = Literal[
    "NONE",
    "CRDR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "CRDR",
    )
)


def serialize_json(value: DataReplicationMode) -> str:
    return value


def deserialize_json(data: str) -> DataReplicationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataReplicationMode value: {data!r}")
    return cast(DataReplicationMode, data)
