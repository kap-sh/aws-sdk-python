"""Generated from Smithy shape ``com.amazonaws.keyspaces#StaticColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.static_column

StaticColumnList: TypeAlias = list["aws_sdk_keyspaces.types.static_column.StaticColumn"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StaticColumnList) -> list:
    import aws_sdk_keyspaces.types.static_column

    out: list = []
    for item in value:
        out.append(aws_sdk_keyspaces.types.static_column.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> StaticColumnList:
    import aws_sdk_keyspaces.types.static_column

    out: StaticColumnList = []
    for item in data:
        out.append(aws_sdk_keyspaces.types.static_column.deserialize_aws_json_1_0(item))
    return out
