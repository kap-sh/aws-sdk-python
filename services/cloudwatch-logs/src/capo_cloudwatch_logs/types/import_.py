"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Import``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.error_message
    import capo_cloudwatch_logs.types.import_filter
    import capo_cloudwatch_logs.types.import_id
    import capo_cloudwatch_logs.types.import_statistics
    import capo_cloudwatch_logs.types.import_status
    import capo_cloudwatch_logs.types.timestamp


class Import(TypedDict, closed=True):
    import_id: NotRequired["capo_cloudwatch_logs.types.import_id.ImportId"]
    """<p>The unique identifier of the import task.</p>"""
    import_source_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the CloudTrail Lake Event Data Store being imported from.</p>"""
    import_status: NotRequired["capo_cloudwatch_logs.types.import_status.ImportStatus"]
    """<p>The current status of the import task. Valid values are IN_PROGRESS, CANCELLED, COMPLETED and FAILED.</p>"""
    import_destination_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the managed CloudWatch Logs log group where the events are being imported to.</p>"""
    import_statistics: NotRequired[
        "capo_cloudwatch_logs.types.import_statistics.ImportStatistics"
    ]
    """<p>Statistics about the import progress</p>"""
    import_filter: NotRequired["capo_cloudwatch_logs.types.import_filter.ImportFilter"]
    """<p>The filter criteria used for this import task.</p>"""
    creation_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp when the import task was created, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.</p>"""
    last_updated_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp when the import task was last updated, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.</p>"""
    error_message: NotRequired["capo_cloudwatch_logs.types.error_message.ErrorMessage"]
    """<p>Error message related to any failed imports</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Import) -> dict:
    out: dict = {}
    if "import_id" in value:
        out["importId"] = value["import_id"]
    if "import_source_arn" in value:
        out["importSourceArn"] = value["import_source_arn"]
    if "import_status" in value:
        import capo_cloudwatch_logs.types.import_status

        out["importStatus"] = (
            capo_cloudwatch_logs.types.import_status.serialize_aws_json_1_1(
                value["import_status"]
            )
        )
    if "import_destination_arn" in value:
        out["importDestinationArn"] = value["import_destination_arn"]
    if "import_statistics" in value:
        import capo_cloudwatch_logs.types.import_statistics

        out["importStatistics"] = (
            capo_cloudwatch_logs.types.import_statistics.serialize_aws_json_1_1(
                value["import_statistics"]
            )
        )
    if "import_filter" in value:
        import capo_cloudwatch_logs.types.import_filter

        out["importFilter"] = (
            capo_cloudwatch_logs.types.import_filter.serialize_aws_json_1_1(
                value["import_filter"]
            )
        )
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Import:
    out: Import = {}  # type: ignore[typeddict-item]
    if "importId" in data:
        out["import_id"] = data["importId"]
    if "importSourceArn" in data:
        out["import_source_arn"] = data["importSourceArn"]
    if "importStatus" in data:
        import capo_cloudwatch_logs.types.import_status

        out["import_status"] = (
            capo_cloudwatch_logs.types.import_status.deserialize_aws_json_1_1(
                data["importStatus"]
            )
        )
    if "importDestinationArn" in data:
        out["import_destination_arn"] = data["importDestinationArn"]
    if "importStatistics" in data:
        import capo_cloudwatch_logs.types.import_statistics

        out["import_statistics"] = (
            capo_cloudwatch_logs.types.import_statistics.deserialize_aws_json_1_1(
                data["importStatistics"]
            )
        )
    if "importFilter" in data:
        import capo_cloudwatch_logs.types.import_filter

        out["import_filter"] = (
            capo_cloudwatch_logs.types.import_filter.deserialize_aws_json_1_1(
                data["importFilter"]
            )
        )
    if "creationTime" in data:
        out["creation_time"] = data["creationTime"]
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
