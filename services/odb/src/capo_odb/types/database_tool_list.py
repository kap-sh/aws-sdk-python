"""Generated from Smithy shape ``com.amazonaws.odb#DatabaseToolList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.database_tool

DatabaseToolList: TypeAlias = list["capo_odb.types.database_tool.DatabaseTool"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatabaseToolList) -> list:
    import capo_odb.types.database_tool

    out: list = []
    for item in value:
        out.append(capo_odb.types.database_tool.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> DatabaseToolList:
    import capo_odb.types.database_tool

    out: DatabaseToolList = []
    for item in data:
        out.append(capo_odb.types.database_tool.deserialize_aws_json_1_0(item))
    return out
