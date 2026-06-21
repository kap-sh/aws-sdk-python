"""Generated from Smithy shape ``com.amazonaws.mq#DataReplicationMode``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies whether a broker is a part of a data replication pair.</p>"""
DataReplicationMode: TypeAlias = Literal[
    "NONE",
    "CRDR",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataReplicationMode) -> str:
    return value


def deserialize_json(data: str) -> DataReplicationMode:
    return cast(DataReplicationMode, data)
