"""Generated from Smithy shape ``com.amazonaws.datapipeline#ReportTaskProgressOutput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.boolean


class ReportTaskProgressOutput(TypedDict):
    canceled: "aws_sdk_data_pipeline.types.boolean.boolean"
    """<p>If true, the calling task runner should cancel processing of the task. The task runner does not need to call <a>SetTaskStatus</a> for canceled tasks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportTaskProgressOutput) -> dict:
    out: dict = {}
    out["canceled"] = value.get("canceled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportTaskProgressOutput:
    out: ReportTaskProgressOutput = {}  # type: ignore[typeddict-item]
    if "canceled" in data:
        out["canceled"] = data["canceled"]
    else:
        out["canceled"] = False
    return out
