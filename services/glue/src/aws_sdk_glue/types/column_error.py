"""Generated from Smithy shape ``com.amazonaws.glue#ColumnError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.error_detail
    import aws_sdk_glue.types.name_string


class ColumnError(TypedDict):
    column_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the column that failed.</p>"""
    error: NotRequired["aws_sdk_glue.types.error_detail.ErrorDetail"]
    """<p>An error message with the reason for the failure of an operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnError) -> dict:
    out: dict = {}
    if "column_name" in value:
        out["ColumnName"] = value["column_name"]
    if "error" in value:
        import aws_sdk_glue.types.error_detail

        out["Error"] = aws_sdk_glue.types.error_detail.serialize_aws_json_1_1(
            value["error"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ColumnError:
    out: ColumnError = {}  # type: ignore[typeddict-item]
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    if "Error" in data:
        import aws_sdk_glue.types.error_detail

        out["error"] = aws_sdk_glue.types.error_detail.deserialize_aws_json_1_1(
            data["Error"]
        )
    return out
