"""Generated from Smithy shape ``com.amazonaws.glue#TableVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.table
    import aws_sdk_glue.types.version_string


class TableVersion(TypedDict, closed=True):
    table: NotRequired["aws_sdk_glue.types.table.Table"]
    """<p>The table in question.</p>"""
    version_id: NotRequired["aws_sdk_glue.types.version_string.VersionString"]
    """<p>The ID value that identifies this table version. A <code>VersionId</code> is a string representation of an integer. Each version is incremented by 1.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableVersion) -> dict:
    out: dict = {}
    if "table" in value:
        import aws_sdk_glue.types.table

        out["Table"] = aws_sdk_glue.types.table.serialize_aws_json_1_1(value["table"])
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TableVersion:
    out: TableVersion = {}  # type: ignore[typeddict-item]
    if "Table" in data:
        import aws_sdk_glue.types.table

        out["table"] = aws_sdk_glue.types.table.deserialize_aws_json_1_1(data["Table"])
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    return out
