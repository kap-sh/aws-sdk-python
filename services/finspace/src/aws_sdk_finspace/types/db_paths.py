"""Generated from Smithy shape ``com.amazonaws.finspace#DbPaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.db_path

DbPaths: TypeAlias = list["aws_sdk_finspace.types.db_path.DbPath"]


# --- restJson1 ser/de ---
def serialize_json(value: DbPaths) -> list:
    return list(value)


def deserialize_json(data: list) -> DbPaths:
    return list(data)
