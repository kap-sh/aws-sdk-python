"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetArchiveExportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mailmanager.types.archive_filters
    import aws_sdk_mailmanager.types.archive_id
    import aws_sdk_mailmanager.types.export_destination_configuration
    import aws_sdk_mailmanager.types.export_max_results
    import aws_sdk_mailmanager.types.export_status


class GetArchiveExportResponse(TypedDict):
    archive_id: NotRequired["aws_sdk_mailmanager.types.archive_id.ArchiveId"]
    """<p>The identifier of the archive the email export was performed from.</p>"""
    filters: NotRequired["aws_sdk_mailmanager.types.archive_filters.ArchiveFilters"]
    """<p>The criteria used to filter emails included in the export.</p>"""
    from_timestamp: NotRequired["datetime.datetime"]
    """<p>The start of the timestamp range the exported emails cover.</p>"""
    to_timestamp: NotRequired["datetime.datetime"]
    """<p>The end of the date range the exported emails cover.</p>"""
    max_results: NotRequired[
        "aws_sdk_mailmanager.types.export_max_results.ExportMaxResults"
    ]
    """<p>The maximum number of email items included in the export.</p>"""
    export_destination_configuration: NotRequired[
        "aws_sdk_mailmanager.types.export_destination_configuration.ExportDestinationConfiguration"
    ]
    """<p>Where the exported emails are being delivered.</p>"""
    status: NotRequired["aws_sdk_mailmanager.types.export_status.ExportStatus"]
    """<p>The current status of the export job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetArchiveExportResponse) -> dict:
    out: dict = {}
    if "archive_id" in value:
        out["ArchiveId"] = value["archive_id"]
    if "filters" in value:
        import aws_sdk_mailmanager.types.archive_filters

        out["Filters"] = (
            aws_sdk_mailmanager.types.archive_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "from_timestamp" in value:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["FromTimestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["from_timestamp"]
            )
        )
    if "to_timestamp" in value:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["ToTimestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["to_timestamp"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "export_destination_configuration" in value:
        import aws_sdk_mailmanager.types.export_destination_configuration

        out["ExportDestinationConfiguration"] = (
            aws_sdk_mailmanager.types.export_destination_configuration.serialize_aws_json_1_0(
                value["export_destination_configuration"]
            )
        )
    if "status" in value:
        import aws_sdk_mailmanager.types.export_status

        out["Status"] = aws_sdk_mailmanager.types.export_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetArchiveExportResponse:
    out: GetArchiveExportResponse = {}  # type: ignore[typeddict-item]
    if "ArchiveId" in data:
        out["archive_id"] = data["ArchiveId"]
    if "Filters" in data:
        import aws_sdk_mailmanager.types.archive_filters

        out["filters"] = (
            aws_sdk_mailmanager.types.archive_filters.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if "FromTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["from_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["FromTimestamp"]
            )
        )
    if "ToTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["to_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["ToTimestamp"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "ExportDestinationConfiguration" in data:
        import aws_sdk_mailmanager.types.export_destination_configuration

        out["export_destination_configuration"] = (
            aws_sdk_mailmanager.types.export_destination_configuration.deserialize_aws_json_1_0(
                data["ExportDestinationConfiguration"]
            )
        )
    if "Status" in data:
        import aws_sdk_mailmanager.types.export_status

        out["status"] = (
            aws_sdk_mailmanager.types.export_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
