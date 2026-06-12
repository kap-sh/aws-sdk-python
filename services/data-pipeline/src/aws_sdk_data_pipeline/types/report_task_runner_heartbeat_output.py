"""Generated from Smithy shape ``com.amazonaws.datapipeline#ReportTaskRunnerHeartbeatOutput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.boolean


class ReportTaskRunnerHeartbeatOutput(TypedDict):
    terminate: "aws_sdk_data_pipeline.types.boolean.boolean"
    """<p>Indicates whether the calling task runner should terminate.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportTaskRunnerHeartbeatOutput) -> dict:
    out: dict = {}
    out["terminate"] = value.get("terminate", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportTaskRunnerHeartbeatOutput:
    out: ReportTaskRunnerHeartbeatOutput = {}  # type: ignore[typeddict-item]
    if "terminate" in data:
        out["terminate"] = data["terminate"]
    else:
        out["terminate"] = False
    return out
