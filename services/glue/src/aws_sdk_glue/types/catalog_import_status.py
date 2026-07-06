"""Generated from Smithy shape ``com.amazonaws.glue#CatalogImportStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.boolean
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.timestamp


class CatalogImportStatus(TypedDict, closed=True):
    import_completed: "aws_sdk_glue.types.boolean.Boolean"
    """<p> <code>True</code> if the migration has completed, or <code>False</code> otherwise.</p>"""
    import_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The time that the migration was started.</p>"""
    imported_by: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the person who initiated the migration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogImportStatus) -> dict:
    out: dict = {}
    out["ImportCompleted"] = value.get("import_completed", False)
    if "import_time" in value:
        import aws_sdk_glue.types.timestamp

        out["ImportTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["import_time"]
        )
    if "imported_by" in value:
        out["ImportedBy"] = value["imported_by"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogImportStatus:
    out: CatalogImportStatus = {}  # type: ignore[typeddict-item]
    if "ImportCompleted" in data:
        out["import_completed"] = data["ImportCompleted"]
    else:
        out["import_completed"] = False
    if "ImportTime" in data:
        import aws_sdk_glue.types.timestamp

        out["import_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["ImportTime"]
        )
    if "ImportedBy" in data:
        out["imported_by"] = data["ImportedBy"]
    return out
