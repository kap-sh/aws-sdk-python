"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StartImportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.date
    import capo_cloudtrail.types.import_destinations
    import capo_cloudtrail.types.import_source
    import capo_cloudtrail.types.import_status
    import capo_cloudtrail.types.uuid


class StartImportResponse(TypedDict, closed=True):
    import_id: NotRequired["capo_cloudtrail.types.uuid.UUID"]
    """<p> The ID of the import. </p>"""
    destinations: NotRequired[
        "capo_cloudtrail.types.import_destinations.ImportDestinations"
    ]
    """<p> The ARN of the destination event data store. </p>"""
    import_source: NotRequired["capo_cloudtrail.types.import_source.ImportSource"]
    """<p> The source S3 bucket for the import. </p>"""
    start_event_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p> Used with <code>EndEventTime</code> to bound a <code>StartImport</code> request, and limit imported trail events to only those events logged within a specified time period. </p>"""
    end_event_time: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p> Used with <code>StartEventTime</code> to bound a <code>StartImport</code> request, and limit imported trail events to only those events logged within a specified time period. </p>"""
    import_status: NotRequired["capo_cloudtrail.types.import_status.ImportStatus"]
    """<p> Shows the status of the import after a <code>StartImport</code> request. An import finishes with a status of <code>COMPLETED</code> if there were no failures, or <code>FAILED</code> if there were failures. </p>"""
    created_timestamp: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p> The timestamp for the import's creation. </p>"""
    updated_timestamp: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p> The timestamp of the import's last update, if applicable. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartImportResponse) -> dict:
    out: dict = {}
    if "import_id" in value:
        out["ImportId"] = value["import_id"]
    if "destinations" in value:
        import capo_cloudtrail.types.import_destinations

        out["Destinations"] = (
            capo_cloudtrail.types.import_destinations.serialize_aws_json_1_1(
                value["destinations"]
            )
        )
    if "import_source" in value:
        import capo_cloudtrail.types.import_source

        out["ImportSource"] = (
            capo_cloudtrail.types.import_source.serialize_aws_json_1_1(
                value["import_source"]
            )
        )
    if "start_event_time" in value:
        import capo_cloudtrail.types.date

        out["StartEventTime"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["start_event_time"]
        )
    if "end_event_time" in value:
        import capo_cloudtrail.types.date

        out["EndEventTime"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["end_event_time"]
        )
    if "import_status" in value:
        import capo_cloudtrail.types.import_status

        out["ImportStatus"] = (
            capo_cloudtrail.types.import_status.serialize_aws_json_1_1(
                value["import_status"]
            )
        )
    if "created_timestamp" in value:
        import capo_cloudtrail.types.date

        out["CreatedTimestamp"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["created_timestamp"]
        )
    if "updated_timestamp" in value:
        import capo_cloudtrail.types.date

        out["UpdatedTimestamp"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["updated_timestamp"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartImportResponse:
    out: StartImportResponse = {}  # type: ignore[typeddict-item]
    if "ImportId" in data:
        out["import_id"] = data["ImportId"]
    if "Destinations" in data:
        import capo_cloudtrail.types.import_destinations

        out["destinations"] = (
            capo_cloudtrail.types.import_destinations.deserialize_aws_json_1_1(
                data["Destinations"]
            )
        )
    if "ImportSource" in data:
        import capo_cloudtrail.types.import_source

        out["import_source"] = (
            capo_cloudtrail.types.import_source.deserialize_aws_json_1_1(
                data["ImportSource"]
            )
        )
    if "StartEventTime" in data:
        import capo_cloudtrail.types.date

        out["start_event_time"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["StartEventTime"]
        )
    if "EndEventTime" in data:
        import capo_cloudtrail.types.date

        out["end_event_time"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["EndEventTime"]
        )
    if "ImportStatus" in data:
        import capo_cloudtrail.types.import_status

        out["import_status"] = (
            capo_cloudtrail.types.import_status.deserialize_aws_json_1_1(
                data["ImportStatus"]
            )
        )
    if "CreatedTimestamp" in data:
        import capo_cloudtrail.types.date

        out["created_timestamp"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["CreatedTimestamp"]
        )
    if "UpdatedTimestamp" in data:
        import capo_cloudtrail.types.date

        out["updated_timestamp"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["UpdatedTimestamp"]
        )
    return out
