"""Generated from Smithy shape ``com.amazonaws.datapipeline#ReportTaskProgressInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.field_list
    import aws_sdk_data_pipeline.types.task_id


class ReportTaskProgressInput(TypedDict, closed=True):
    task_id: "aws_sdk_data_pipeline.types.task_id.taskId"
    """<p>The ID of the task assigned to the task runner. This value is provided in the response for <a>PollForTask</a>.</p>"""
    fields: NotRequired["aws_sdk_data_pipeline.types.field_list.fieldList"]
    """<p>Key-value pairs that define the properties of the ReportTaskProgressInput object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportTaskProgressInput) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    if "fields" in value:
        import aws_sdk_data_pipeline.types.field_list

        out["fields"] = aws_sdk_data_pipeline.types.field_list.serialize_aws_json_1_1(
            value["fields"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportTaskProgressInput:
    out: ReportTaskProgressInput = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("ReportTaskProgressInput.task_id required")
    if "fields" in data:
        import aws_sdk_data_pipeline.types.field_list

        out["fields"] = aws_sdk_data_pipeline.types.field_list.deserialize_aws_json_1_1(
            data["fields"]
        )
    return out
