"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetImportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.date
    import aws_sdk_cloudtrail.types.import_destinations
    import aws_sdk_cloudtrail.types.import_source
    import aws_sdk_cloudtrail.types.import_statistics
    import aws_sdk_cloudtrail.types.import_status
    import aws_sdk_cloudtrail.types.uuid


class GetImportResponse(TypedDict, closed=True):
    import_id: NotRequired["aws_sdk_cloudtrail.types.uuid.UUID"]
    """<p> The ID of the import. </p>"""
    destinations: NotRequired[
        "aws_sdk_cloudtrail.types.import_destinations.ImportDestinations"
    ]
    """<p> The ARN of the destination event data store. </p>"""
    import_source: NotRequired["aws_sdk_cloudtrail.types.import_source.ImportSource"]
    """<p> The source S3 bucket. </p>"""
    start_event_time: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p> Used with <code>EndEventTime</code> to bound a <code>StartImport</code> request, and limit imported trail events to only those events logged within a specified time period. </p>"""
    end_event_time: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p> Used with <code>StartEventTime</code> to bound a <code>StartImport</code> request, and limit imported trail events to only those events logged within a specified time period. </p>"""
    import_status: NotRequired["aws_sdk_cloudtrail.types.import_status.ImportStatus"]
    """<p> The status of the import. </p>"""
    created_timestamp: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p> The timestamp of the import's creation. </p>"""
    updated_timestamp: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p> The timestamp of when the import was updated. </p>"""
    import_statistics: NotRequired[
        "aws_sdk_cloudtrail.types.import_statistics.ImportStatistics"
    ]
    """<p> Provides statistics for the import. CloudTrail does not update import statistics in real-time. Returned values for parameters such as <code>EventsCompleted</code> may be lower than the actual value, because CloudTrail updates statistics incrementally over the course of the import. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetImportResponse) -> dict:
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
    if "import_statistics" in value:
        import aws_sdk_cloudtrail.types.import_statistics

        out["ImportStatistics"] = (
            aws_sdk_cloudtrail.types.import_statistics.serialize_aws_json_1_1(
                value["import_statistics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetImportResponse:
    out: GetImportResponse = {}  # type: ignore[typeddict-item]
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
    if "ImportStatistics" in data:
        import aws_sdk_cloudtrail.types.import_statistics

        out["import_statistics"] = (
            aws_sdk_cloudtrail.types.import_statistics.deserialize_aws_json_1_1(
                data["ImportStatistics"]
            )
        )
    return out
