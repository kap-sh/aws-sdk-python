"""Generated from Smithy shape ``com.amazonaws.mgn#ImportIDsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.import_id

ImportIDsFilter: TypeAlias = list["aws_sdk_mgn.types.import_id.ImportID"]


# --- restJson1 ser/de ---
def serialize_json(value: ImportIDsFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> ImportIDsFilter:
    return list(data)
