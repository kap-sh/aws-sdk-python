"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UpdateExportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.export_resource_specification
    import aws_sdk_lex_models_v2.types.export_status
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.import_export_file_format
    import aws_sdk_lex_models_v2.types.timestamp


class UpdateExportResponse(TypedDict):
    export_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier Amazon Lex assigned to the export.</p>"""
    resource_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.export_resource_specification.ExportResourceSpecification"
    ]
    """<p>A description of the type of resource that was exported, either a bot or a bot locale.</p>"""
    file_format: NotRequired[
        "aws_sdk_lex_models_v2.types.import_export_file_format.ImportExportFileFormat"
    ]
    """<p>The file format used for the files that define the resource. The <code>TSV</code> format is required to export a custom vocabulary only; otherwise use <code>LexJson</code> format.</p>"""
    export_status: NotRequired["aws_sdk_lex_models_v2.types.export_status.ExportStatus"]
    """<p>The status of the export. When the status is <code>Completed</code> the export archive is available for download.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the export was created.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The date and time that the export was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateExportResponse) -> dict:
    out: dict = {}
    if "export_id" in value:
        out["exportId"] = value["export_id"]
    if "resource_specification" in value:
        import aws_sdk_lex_models_v2.types.export_resource_specification

        out["resourceSpecification"] = (
            aws_sdk_lex_models_v2.types.export_resource_specification.serialize_json(
                value["resource_specification"]
            )
        )
    if "file_format" in value:
        import aws_sdk_lex_models_v2.types.import_export_file_format

        out["fileFormat"] = (
            aws_sdk_lex_models_v2.types.import_export_file_format.serialize_json(
                value["file_format"]
            )
        )
    if "export_status" in value:
        import aws_sdk_lex_models_v2.types.export_status

        out["exportStatus"] = aws_sdk_lex_models_v2.types.export_status.serialize_json(
            value["export_status"]
        )
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["last_updated_date_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateExportResponse:
    out: UpdateExportResponse = {}  # type: ignore[typeddict-item]
    if "exportId" in data:
        out["export_id"] = data["exportId"]
    if "resourceSpecification" in data:
        import aws_sdk_lex_models_v2.types.export_resource_specification

        out["resource_specification"] = (
            aws_sdk_lex_models_v2.types.export_resource_specification.deserialize_json(
                data["resourceSpecification"]
            )
        )
    if "fileFormat" in data:
        import aws_sdk_lex_models_v2.types.import_export_file_format

        out["file_format"] = (
            aws_sdk_lex_models_v2.types.import_export_file_format.deserialize_json(
                data["fileFormat"]
            )
        )
    if "exportStatus" in data:
        import aws_sdk_lex_models_v2.types.export_status

        out["export_status"] = (
            aws_sdk_lex_models_v2.types.export_status.deserialize_json(
                data["exportStatus"]
            )
        )
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    return out
