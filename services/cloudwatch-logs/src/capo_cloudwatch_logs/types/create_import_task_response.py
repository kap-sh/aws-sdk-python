"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateImportTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.import_id
    import capo_cloudwatch_logs.types.timestamp


class CreateImportTaskResponse(TypedDict, closed=True):
    import_id: NotRequired["capo_cloudwatch_logs.types.import_id.ImportId"]
    """<p>A unique identifier for the import task.</p>"""
    import_destination_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the CloudWatch Logs log group created as the destination for the imported events.</p>"""
    creation_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The timestamp when the import task was created, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateImportTaskResponse) -> dict:
    out: dict = {}
    if "import_id" in value:
        out["importId"] = value["import_id"]
    if "import_destination_arn" in value:
        out["importDestinationArn"] = value["import_destination_arn"]
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateImportTaskResponse:
    out: CreateImportTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("importId") is not None:
        out["import_id"] = data["importId"]
    if data.get("importDestinationArn") is not None:
        out["import_destination_arn"] = data["importDestinationArn"]
    if data.get("creationTime") is not None:
        out["creation_time"] = data["creationTime"]
    return out
