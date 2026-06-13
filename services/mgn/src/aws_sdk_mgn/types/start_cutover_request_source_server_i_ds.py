"""Generated from Smithy shape ``com.amazonaws.mgn#StartCutoverRequestSourceServerIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.source_server_id

StartCutoverRequestSourceServerIDs: TypeAlias = list[
    "aws_sdk_mgn.types.source_server_id.SourceServerID"
]


# --- restJson1 ser/de ---
def serialize_json(value: StartCutoverRequestSourceServerIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> StartCutoverRequestSourceServerIDs:
    return list(data)
