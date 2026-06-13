"""Generated from Smithy shape ``com.amazonaws.redshiftdata#TableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.table_member

TableList: TypeAlias = list["aws_sdk_redshift_data.types.table_member.TableMember"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableList) -> list:
    import aws_sdk_redshift_data.types.table_member

    out: list = []
    for item in value:
        out.append(
            aws_sdk_redshift_data.types.table_member.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TableList:
    import aws_sdk_redshift_data.types.table_member

    out: TableList = []
    for item in data:
        out.append(
            aws_sdk_redshift_data.types.table_member.deserialize_aws_json_1_1(item)
        )
    return out
