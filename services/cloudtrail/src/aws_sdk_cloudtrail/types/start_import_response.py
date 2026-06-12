"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StartImportResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.date
    import aws_sdk_cloudtrail.types.import_destinations
    import aws_sdk_cloudtrail.types.import_source
    import aws_sdk_cloudtrail.types.import_status
    import aws_sdk_cloudtrail.types.uuid


class StartImportResponse(TypedDict):
    import_id: NotRequired["aws_sdk_cloudtrail.types.uuid.UUID"]
    """<p> The ID of the import. </p>"""
    destinations: NotRequired[
        "aws_sdk_cloudtrail.types.import_destinations.ImportDestinations"
    ]
    """<p> The ARN of the destination event data store. </p>"""
    import_source: NotRequired["aws_sdk_cloudtrail.types.import_source.ImportSource"]
    """<p> The source S3 bucket for the import. </p>"""
    start_event_time: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p> Used with <code>EndEventTime</code> to bound a <code>StartImport</code> request, and limit imported trail events to only those events logged within a specified time period. </p>"""
    end_event_time: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p> Used with <code>StartEventTime</code> to bound a <code>StartImport</code> request, and limit imported trail events to only those events logged within a specified time period. </p>"""
    import_status: NotRequired["aws_sdk_cloudtrail.types.import_status.ImportStatus"]
    """<p> Shows the status of the import after a <code>StartImport</code> request. An import finishes with a status of <code>COMPLETED</code> if there were no failures, or <code>FAILED</code> if there were failures. </p>"""
    created_timestamp: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p> The timestamp for the import's creation. </p>"""
    updated_timestamp: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p> The timestamp of the import's last update, if applicable. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartImportResponse) -> dict:
    out: dict = {}
    if "import_id" in value:
        out["ImportId"] = value["import_id"]
    if "destinations" in value:
        import aws_sdk_cloudtrail.types.import_destinations

        out["Destinations"] = (
            aws_sdk_cloudtrail.types.import_destinations.serialize_aws_json_1_1(
                value["destinations"]
            )
        )
    if "import_source" in value:
        import aws_sdk_cloudtrail.types.import_source

        out["ImportSource"] = (
            aws_sdk_cloudtrail.types.import_source.serialize_aws_json_1_1(
                value["import_source"]
            )
        )
    if "start_event_time" in value:
        import aws_sdk_cloudtrail.types.date

        out["StartEventTime"] = aws_sdk_cloudtrail.types.date.serialize_aws_json_1_1(
            value["start_event_time"]
        )
    if "end_event_time" in value:
        import aws_sdk_cloudtrail.types.date

        out["EndEventTime"] = aws_sdk_cloudtrail.types.date.serialize_aws_json_1_1(
            value["end_event_time"]
        )
    if "import_status" in value:
        import aws_sdk_cloudtrail.types.import_status

        out["ImportStatus"] = (
            aws_sdk_cloudtrail.types.import_status.serialize_aws_json_1_1(
                value["import_status"]
            )
        )
    if "created_timestamp" in value:
        import aws_sdk_cloudtrail.types.date

        out["CreatedTimestamp"] = aws_sdk_cloudtrail.types.date.serialize_aws_json_1_1(
            value["created_timestamp"]
        )
    if "updated_timestamp" in value:
        import aws_sdk_cloudtrail.types.date

        out["UpdatedTimestamp"] = aws_sdk_cloudtrail.types.date.serialize_aws_json_1_1(
            value["updated_timestamp"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartImportResponse:
    out: StartImportResponse = {}  # type: ignore[typeddict-item]
    if "ImportId" in data:
        out["import_id"] = data["ImportId"]
    if "Destinations" in data:
        import aws_sdk_cloudtrail.types.import_destinations

        out["destinations"] = (
            aws_sdk_cloudtrail.types.import_destinations.deserialize_aws_json_1_1(
                data["Destinations"]
            )
        )
    if "ImportSource" in data:
        import aws_sdk_cloudtrail.types.import_source

        out["import_source"] = (
            aws_sdk_cloudtrail.types.import_source.deserialize_aws_json_1_1(
                data["ImportSource"]
            )
        )
    if "StartEventTime" in data:
        import aws_sdk_cloudtrail.types.date

        out["start_event_time"] = (
            aws_sdk_cloudtrail.types.date.deserialize_aws_json_1_1(
                data["StartEventTime"]
            )
        )
    if "EndEventTime" in data:
        import aws_sdk_cloudtrail.types.date

        out["end_event_time"] = aws_sdk_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["EndEventTime"]
        )
    if "ImportStatus" in data:
        import aws_sdk_cloudtrail.types.import_status

        out["import_status"] = (
            aws_sdk_cloudtrail.types.import_status.deserialize_aws_json_1_1(
                data["ImportStatus"]
            )
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_cloudtrail.types.date

        out["created_timestamp"] = (
            aws_sdk_cloudtrail.types.date.deserialize_aws_json_1_1(
                data["CreatedTimestamp"]
            )
        )
    if "UpdatedTimestamp" in data:
        import aws_sdk_cloudtrail.types.date

        out["updated_timestamp"] = (
            aws_sdk_cloudtrail.types.date.deserialize_aws_json_1_1(
                data["UpdatedTimestamp"]
            )
        )
    return out
