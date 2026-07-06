"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StartImportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.date
    import aws_sdk_cloudtrail.types.import_destinations
    import aws_sdk_cloudtrail.types.import_source
    import aws_sdk_cloudtrail.types.uuid


class StartImportRequest(TypedDict, closed=True):
    destinations: NotRequired[
        "aws_sdk_cloudtrail.types.import_destinations.ImportDestinations"
    ]
    """<p> The ARN of the destination event data store. Use this parameter for a new import. </p>"""
    import_source: NotRequired["aws_sdk_cloudtrail.types.import_source.ImportSource"]
    """<p> The source S3 bucket for the import. Use this parameter for a new import. </p>"""
    start_event_time: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p> Use with <code>EndEventTime</code> to bound a <code>StartImport</code> request, and limit imported trail events to only those events logged within a specified time period. When you specify a time range, CloudTrail checks the prefix and log file names to verify the names contain a date between the specified <code>StartEventTime</code> and <code>EndEventTime</code> before attempting to import events. </p>"""
    end_event_time: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p> Use with <code>StartEventTime</code> to bound a <code>StartImport</code> request, and limit imported trail events to only those events logged within a specified time period. When you specify a time range, CloudTrail checks the prefix and log file names to verify the names contain a date between the specified <code>StartEventTime</code> and <code>EndEventTime</code> before attempting to import events. </p>"""
    import_id: NotRequired["aws_sdk_cloudtrail.types.uuid.UUID"]
    """<p> The ID of the import. Use this parameter when you are retrying an import. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartImportRequest) -> dict:
    out: dict = {}
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
    if "import_id" in value:
        out["ImportId"] = value["import_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartImportRequest:
    out: StartImportRequest = {}  # type: ignore[typeddict-item]
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
    if "ImportId" in data:
        out["import_id"] = data["ImportId"]
    return out
