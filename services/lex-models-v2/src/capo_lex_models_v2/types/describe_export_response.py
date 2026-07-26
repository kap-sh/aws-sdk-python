"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.export_resource_specification
    import capo_lex_models_v2.types.export_status
    import capo_lex_models_v2.types.failure_reasons
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.import_export_file_format
    import capo_lex_models_v2.types.presigned_s3_url
    import capo_lex_models_v2.types.timestamp


class DescribeExportResponse(TypedDict, closed=True):
    export_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the described export.</p>"""
    resource_specification: NotRequired[
        "capo_lex_models_v2.types.export_resource_specification.ExportResourceSpecification"
    ]
    """<p>The bot, bot ID, and optional locale ID of the exported bot or bot locale.</p>"""
    file_format: NotRequired[
        "capo_lex_models_v2.types.import_export_file_format.ImportExportFileFormat"
    ]
    """<p>The file format used in the files that describe the resource. </p>"""
    export_status: NotRequired["capo_lex_models_v2.types.export_status.ExportStatus"]
    """<p>The status of the export. When the status is <code>Complete</code> the export archive file is available for download.</p>"""
    failure_reasons: NotRequired[
        "capo_lex_models_v2.types.failure_reasons.FailureReasons"
    ]
    """<p>If the <code>exportStatus</code> is failed, contains one or more reasons why the export could not be completed.</p>"""
    download_url: NotRequired[
        "capo_lex_models_v2.types.presigned_s3_url.PresignedS3Url"
    ]
    """<p>A pre-signed S3 URL that points to the bot or bot locale archive. The URL is only available for 5 minutes after calling the <code>DescribeExport</code> operation.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the export was created.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The last date and time that the export was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeExportResponse) -> dict:
    out: dict = {}
    if "export_id" in value:
        out["exportId"] = value["export_id"]
    if "resource_specification" in value:
        import capo_lex_models_v2.types.export_resource_specification

        out["resourceSpecification"] = (
            capo_lex_models_v2.types.export_resource_specification.serialize_json(
                value["resource_specification"]
            )
        )
    if "file_format" in value:
        import capo_lex_models_v2.types.import_export_file_format

        out["fileFormat"] = (
            capo_lex_models_v2.types.import_export_file_format.serialize_json(
                value["file_format"]
            )
        )
    if "export_status" in value:
        import capo_lex_models_v2.types.export_status

        out["exportStatus"] = capo_lex_models_v2.types.export_status.serialize_json(
            value["export_status"]
        )
    if "failure_reasons" in value:
        import capo_lex_models_v2.types.failure_reasons

        out["failureReasons"] = capo_lex_models_v2.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    if "download_url" in value:
        out["downloadUrl"] = value["download_url"]
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["last_updated_date_time"]
        )
    return out


def deserialize_json(data: dict) -> DescribeExportResponse:
    out: DescribeExportResponse = {}  # type: ignore[typeddict-item]
    if "exportId" in data:
        out["export_id"] = data["exportId"]
    if "resourceSpecification" in data:
        import capo_lex_models_v2.types.export_resource_specification

        out["resource_specification"] = (
            capo_lex_models_v2.types.export_resource_specification.deserialize_json(
                data["resourceSpecification"]
            )
        )
    if "fileFormat" in data:
        import capo_lex_models_v2.types.import_export_file_format

        out["file_format"] = (
            capo_lex_models_v2.types.import_export_file_format.deserialize_json(
                data["fileFormat"]
            )
        )
    if "exportStatus" in data:
        import capo_lex_models_v2.types.export_status

        out["export_status"] = capo_lex_models_v2.types.export_status.deserialize_json(
            data["exportStatus"]
        )
    if "failureReasons" in data:
        import capo_lex_models_v2.types.failure_reasons

        out["failure_reasons"] = (
            capo_lex_models_v2.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    if "downloadUrl" in data:
        out["download_url"] = data["downloadUrl"]
    if "creationDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if "lastUpdatedDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    return out
