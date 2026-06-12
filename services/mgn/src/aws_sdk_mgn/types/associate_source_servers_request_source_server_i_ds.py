"""Generated from Smithy shape ``com.amazonaws.mgn#AssociateSourceServersRequestSourceServerIDs``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_mgn.types.source_server_id

AssociateSourceServersRequestSourceServerIDs: TypeAlias = list["aws_sdk_mgn.types.source_server_id.SourceServerID"]


# --- restJson1 ser/de ---
def serialize_json(value: AssociateSourceServersRequestSourceServerIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> AssociateSourceServersRequestSourceServerIDs:
    return list(data)