"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceRunLineageSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.lineage_import_status


class DataSourceRunLineageSummary(TypedDict, closed=True):
    import_status: NotRequired[
        "aws_sdk_datazone.types.lineage_import_status.LineageImportStatus"
    ]
    """<p>The import status that's part of the run lineage summary of a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceRunLineageSummary) -> dict:
    out: dict = {}
    if "import_status" in value:
        import aws_sdk_datazone.types.lineage_import_status

        out["importStatus"] = (
            aws_sdk_datazone.types.lineage_import_status.serialize_json(
                value["import_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSourceRunLineageSummary:
    out: DataSourceRunLineageSummary = {}  # type: ignore[typeddict-item]
    if "importStatus" in data:
        import aws_sdk_datazone.types.lineage_import_status

        out["import_status"] = (
            aws_sdk_datazone.types.lineage_import_status.deserialize_json(
                data["importStatus"]
            )
        )
    return out
