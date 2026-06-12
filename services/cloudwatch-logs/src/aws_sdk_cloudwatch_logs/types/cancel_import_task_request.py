"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CancelImportTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.import_id


class CancelImportTaskRequest(TypedDict):
    import_id: "aws_sdk_cloudwatch_logs.types.import_id.ImportId"
    """<p>The ID of the import task to cancel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelImportTaskRequest) -> dict:
    out: dict = {}
    out["importId"] = value["import_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelImportTaskRequest:
    out: CancelImportTaskRequest = {}  # type: ignore[typeddict-item]
    if "importId" in data:
        out["import_id"] = data["importId"]
    else:
        raise DeserializationError("CancelImportTaskRequest.import_id required")
    return out
