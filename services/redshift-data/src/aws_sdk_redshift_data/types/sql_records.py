"""Generated from Smithy shape ``com.amazonaws.redshiftdata#SqlRecords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.field_list

SqlRecords: TypeAlias = list["aws_sdk_redshift_data.types.field_list.FieldList"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlRecords) -> list:
    import aws_sdk_redshift_data.types.field_list

    out: list = []
    for item in value:
        out.append(aws_sdk_redshift_data.types.field_list.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SqlRecords:
    import aws_sdk_redshift_data.types.field_list

    out: SqlRecords = []
    for item in data:
        out.append(
            aws_sdk_redshift_data.types.field_list.deserialize_aws_json_1_1(item)
        )
    return out
