"""Generated from Smithy shape ``com.amazonaws.keyspaces#TableNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_keyspaces.types.table_name

TableNameList: TypeAlias = list["capo_keyspaces.types.table_name.TableName"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TableNameList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> TableNameList:
    return list(data)
