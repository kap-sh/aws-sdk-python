"""Generated from Smithy shape ``com.amazonaws.drs#StagingSourceServersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.staging_source_server

StagingSourceServersList: TypeAlias = list[
    "aws_sdk_drs.types.staging_source_server.StagingSourceServer"
]


# --- restJson1 ser/de ---
def serialize_json(value: StagingSourceServersList) -> list:
    import aws_sdk_drs.types.staging_source_server

    out: list = []
    for item in value:
        out.append(aws_sdk_drs.types.staging_source_server.serialize_json(item))
    return out


def deserialize_json(data: list) -> StagingSourceServersList:
    import aws_sdk_drs.types.staging_source_server

    out: StagingSourceServersList = []
    for item in data:
        out.append(aws_sdk_drs.types.staging_source_server.deserialize_json(item))
    return out
