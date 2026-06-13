"""Generated from Smithy shape ``com.amazonaws.redshiftdata#FieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_data.types.field

FieldList: TypeAlias = list["aws_sdk_redshift_data.types.field.Field"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldList) -> list:
    import aws_sdk_redshift_data.types.field

    out: list = []
    for item in value:
        out.append(aws_sdk_redshift_data.types.field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FieldList:
    import aws_sdk_redshift_data.types.field

    out: FieldList = []
    for item in data:
        out.append(aws_sdk_redshift_data.types.field.deserialize_aws_json_1_1(item))
    return out
