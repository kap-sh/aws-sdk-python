"""Generated from Smithy shape ``com.amazonaws.drs#SourceServersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.source_server

SourceServersList: TypeAlias = list["aws_sdk_drs.types.source_server.SourceServer"]


# --- restJson1 ser/de ---
def serialize_json(value: SourceServersList) -> list:
    import aws_sdk_drs.types.source_server

    out: list = []
    for item in value:
        out.append(aws_sdk_drs.types.source_server.serialize_json(item))
    return out


def deserialize_json(data: list) -> SourceServersList:
    import aws_sdk_drs.types.source_server

    out: SourceServersList = []
    for item in data:
        out.append(aws_sdk_drs.types.source_server.deserialize_json(item))
    return out
