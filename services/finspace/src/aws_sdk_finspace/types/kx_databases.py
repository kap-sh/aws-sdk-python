"""Generated from Smithy shape ``com.amazonaws.finspace#KxDatabases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_database_list_entry

KxDatabases: TypeAlias = list[
    "aws_sdk_finspace.types.kx_database_list_entry.KxDatabaseListEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxDatabases) -> list:
    import aws_sdk_finspace.types.kx_database_list_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_finspace.types.kx_database_list_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> KxDatabases:
    import aws_sdk_finspace.types.kx_database_list_entry

    out: KxDatabases = []
    for item in data:
        out.append(aws_sdk_finspace.types.kx_database_list_entry.deserialize_json(item))
    return out
