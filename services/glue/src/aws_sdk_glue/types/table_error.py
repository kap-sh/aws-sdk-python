"""Generated from Smithy shape ``com.amazonaws.glue#TableError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.error_detail
    import aws_sdk_glue.types.name_string


class TableError(TypedDict):
    table_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the table. For Hive compatibility, this must be entirely lowercase.</p>"""
    error_detail: NotRequired["aws_sdk_glue.types.error_detail.ErrorDetail"]
    """<p>The details about the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableError) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "error_detail" in value:
        import aws_sdk_glue.types.error_detail

        out["ErrorDetail"] = aws_sdk_glue.types.error_detail.serialize_aws_json_1_1(
            value["error_detail"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TableError:
    out: TableError = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "ErrorDetail" in data:
        import aws_sdk_glue.types.error_detail

        out["error_detail"] = aws_sdk_glue.types.error_detail.deserialize_aws_json_1_1(
            data["ErrorDetail"]
        )
    return out
