"""Generated from Smithy shape ``com.amazonaws.codepipeline#LatestInPipelineExecutionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_execution_id
    import capo_codepipeline.types.start_time_range


class LatestInPipelineExecutionFilter(TypedDict, closed=True):
    pipeline_execution_id: (
        "capo_codepipeline.types.pipeline_execution_id.PipelineExecutionId"
    )
    """<p>The execution ID for the latest execution in the pipeline.</p>"""
    start_time_range: "capo_codepipeline.types.start_time_range.StartTimeRange"
    """<p>The start time to filter on for the latest execution in the pipeline. Valid options:</p> <ul> <li> <p>All</p> </li> <li> <p>Latest</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LatestInPipelineExecutionFilter) -> dict:
    out: dict = {}
    out["pipelineExecutionId"] = value["pipeline_execution_id"]
    import capo_codepipeline.types.start_time_range

    out["startTimeRange"] = (
        capo_codepipeline.types.start_time_range.serialize_aws_json_1_1(
            value["start_time_range"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> LatestInPipelineExecutionFilter:
    out: LatestInPipelineExecutionFilter = {}  # type: ignore[typeddict-item]
    if "pipelineExecutionId" in data:
        out["pipeline_execution_id"] = data["pipelineExecutionId"]
    else:
        raise DeserializationError(
            "LatestInPipelineExecutionFilter.pipeline_execution_id required"
        )
    if "startTimeRange" in data:
        import capo_codepipeline.types.start_time_range

        out["start_time_range"] = (
            capo_codepipeline.types.start_time_range.deserialize_aws_json_1_1(
                data["startTimeRange"]
            )
        )
    else:
        raise DeserializationError(
            "LatestInPipelineExecutionFilter.start_time_range required"
        )
    return out
