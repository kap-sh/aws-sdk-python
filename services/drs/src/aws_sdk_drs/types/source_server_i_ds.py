"""Generated from Smithy shape ``com.amazonaws.drs#SourceServerIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.source_server_id

SourceServerIDs: TypeAlias = list["aws_sdk_drs.types.source_server_id.SourceServerID"]


# --- restJson1 ser/de ---
def serialize_json(value: SourceServerIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> SourceServerIDs:
    return list(data)
