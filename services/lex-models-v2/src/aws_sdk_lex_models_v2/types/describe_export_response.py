"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeExportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.export_resource_specification
    import aws_sdk_lex_models_v2.types.export_status
    import aws_sdk_lex_models_v2.types.failure_reasons
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.import_export_file_format
    import aws_sdk_lex_models_v2.types.presigned_s3_url
    import aws_sdk_lex_models_v2.types.timestamp


class DescribeExportResponse(TypedDict):
    export_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the described export.</p>"""
    resource_specification: NotRequired[
        "aws_sdk_lex_models_v2.types.export_resource_specification.ExportResourceSpecification"
    ]
    """<p>The bot, bot ID, and optional locale ID of the exported bot or bot locale.</p>"""
    file_format: NotRequired[
        "aws_sdk_lex_models_v2.types.import_export_file_format.ImportExportFileFormat"
    ]
    """<p>The file format used in the files that describe the resource. </p>"""
    export_status: NotRequired["aws_sdk_lex_models_v2.types.export_status.ExportStatus"]
    """<p>The status of the export. When the status is <code>Complete</code> the export archive file is available for download.</p>"""
    failure_reasons: NotRequired[
        "aws_sdk_lex_models_v2.types.failure_reasons.FailureReasons"
    ]
    """<p>If the <code>exportStatus</code> is failed, contains one or more reasons why the export could not be completed.</p>"""
    download_url: NotRequired[
        "aws_sdk_lex_models_v2.types.presigned_s3_url.PresignedS3Url"
    ]
    """<p>A pre-signed S3 URL that points to the bot or bot locale archive. The URL is only available for 5 minutes after calling the <code>DescribeExport</code> operation.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the export was created.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The last date and time that the export was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeExportResponse) -> dict:
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
    if "failure_reasons" in value:
        import aws_sdk_lex_models_v2.types.failure_reasons

        out["failureReasons"] = (
            aws_sdk_lex_models_v2.types.failure_reasons.serialize_json(
                value["failure_reasons"]
            )
        )
    if "download_url" in value:
        out["downloadUrl"] = value["download_url"]
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


def deserialize_json(data: dict) -> DescribeExportResponse:
    out: DescribeExportResponse = {}  # type: ignore[typeddict-item]
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
    if "failureReasons" in data:
        import aws_sdk_lex_models_v2.types.failure_reasons

        out["failure_reasons"] = (
            aws_sdk_lex_models_v2.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    if "downloadUrl" in data:
        out["download_url"] = data["downloadUrl"]
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
