"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CancelImportTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.import_id
    import aws_sdk_cloudwatch_logs.types.import_statistics
    import aws_sdk_cloudwatch_logs.types.import_status
    import aws_sdk_cloudwatch_logs.types.timestamp


class CancelImportTaskResponse(TypedDict, closed=True):
    import_id: NotRequired["aws_sdk_cloudwatch_logs.types.import_id.ImportId"]
    """<p>The ID of the cancelled import task.</p>"""
    import_statistics: NotRequired[
        "aws_sdk_cloudwatch_logs.types.import_statistics.ImportStatistics"
    ]
    """<p>Statistics about the import progress at the time of cancellation.</p>"""
    import_status: NotRequired[
        "aws_sdk_cloudwatch_logs.types.import_status.ImportStatus"
    ]
    """<p>The final status of the import task. This will be set to CANCELLED.</p>"""
    creation_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp when the import task was created, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.</p>"""
    last_updated_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp when the import task was cancelled, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelImportTaskResponse) -> dict:
    out: dict = {}
    if "import_id" in value:
        out["importId"] = value["import_id"]
    if "import_statistics" in value:
        import aws_sdk_cloudwatch_logs.types.import_statistics

        out["importStatistics"] = (
            aws_sdk_cloudwatch_logs.types.import_statistics.serialize_aws_json_1_1(
                value["import_statistics"]
            )
        )
    if "import_status" in value:
        import aws_sdk_cloudwatch_logs.types.import_status

        out["importStatus"] = (
            aws_sdk_cloudwatch_logs.types.import_status.serialize_aws_json_1_1(
                value["import_status"]
            )
        )
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelImportTaskResponse:
    out: CancelImportTaskResponse = {}  # type: ignore[typeddict-item]
    if "importId" in data:
        out["import_id"] = data["importId"]
    if "importStatistics" in data:
        import aws_sdk_cloudwatch_logs.types.import_statistics

        out["import_statistics"] = (
            aws_sdk_cloudwatch_logs.types.import_statistics.deserialize_aws_json_1_1(
                data["importStatistics"]
            )
        )
    if "importStatus" in data:
        import aws_sdk_cloudwatch_logs.types.import_status

        out["import_status"] = (
            aws_sdk_cloudwatch_logs.types.import_status.deserialize_aws_json_1_1(
                data["importStatus"]
            )
        )
    if "creationTime" in data:
        out["creation_time"] = data["creationTime"]
    if "lastUpdatedTime" in data:
        out["last_updated_time"] = data["lastUpdatedTime"]
    return out
