"""Generated from Smithy shape ``com.amazonaws.glue#TableErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.table_error

TableErrors: TypeAlias = list["aws_sdk_glue.types.table_error.TableError"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableErrors) -> list:
    import aws_sdk_glue.types.table_error

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.table_error.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TableErrors:
    import aws_sdk_glue.types.table_error

    out: TableErrors = []
    for item in data:
        out.append(aws_sdk_glue.types.table_error.deserialize_aws_json_1_1(item))
    return out
