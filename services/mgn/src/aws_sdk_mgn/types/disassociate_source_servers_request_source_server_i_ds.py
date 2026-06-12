"""Generated from Smithy shape ``com.amazonaws.mgn#DisassociateSourceServersRequestSourceServerIDs``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_mgn.types.source_server_id

DisassociateSourceServersRequestSourceServerIDs: TypeAlias = list["aws_sdk_mgn.types.source_server_id.SourceServerID"]


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateSourceServersRequestSourceServerIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> DisassociateSourceServersRequestSourceServerIDs:
    return list(data)