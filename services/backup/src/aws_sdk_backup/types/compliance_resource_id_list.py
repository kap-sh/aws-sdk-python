"""Generated from Smithy shape ``com.amazonaws.backup#ComplianceResourceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.string

ComplianceResourceIdList: TypeAlias = list["aws_sdk_backup.types.string.string"]


# --- restJson1 ser/de ---
def serialize_json(value: ComplianceResourceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ComplianceResourceIdList:
    return list(data)
