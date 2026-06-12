"""Generated from Smithy shape ``com.amazonaws.glue#TableVersionError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.error_detail
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.version_string


class TableVersionError(TypedDict):
    table_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the table in question.</p>"""
    version_id: NotRequired["aws_sdk_glue.types.version_string.VersionString"]
    """<p>The ID value of the version in question. A <code>VersionID</code> is a string representation of an integer. Each version is incremented by 1.</p>"""
    error_detail: NotRequired["aws_sdk_glue.types.error_detail.ErrorDetail"]
    """<p>The details about the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableVersionError) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "error_detail" in value:
        import aws_sdk_glue.types.error_detail

        out["ErrorDetail"] = aws_sdk_glue.types.error_detail.serialize_aws_json_1_1(
            value["error_detail"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TableVersionError:
    out: TableVersionError = {}  # type: ignore[typeddict-item]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    if "ErrorDetail" in data:
        import aws_sdk_glue.types.error_detail

        out["error_detail"] = aws_sdk_glue.types.error_detail.deserialize_aws_json_1_1(
            data["ErrorDetail"]
        )
    return out
