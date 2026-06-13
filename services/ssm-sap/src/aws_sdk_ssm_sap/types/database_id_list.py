"""Generated from Smithy shape ``com.amazonaws.ssmsap#DatabaseIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.database_id

DatabaseIdList: TypeAlias = list["aws_sdk_ssm_sap.types.database_id.DatabaseId"]


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> DatabaseIdList:
    return list(data)
