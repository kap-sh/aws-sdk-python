"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PipelineLoggingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.log_group_name


class PipelineLoggingConfiguration(TypedDict):
    image_log_group_name: NotRequired[
        "aws_sdk_imagebuilder.types.log_group_name.LogGroupName"
    ]
    """<p>The log group name that Image Builder uses for image creation. If not specified, the log group name defaults to <code>/aws/imagebuilder/image-name</code>.</p>"""
    pipeline_log_group_name: NotRequired[
        "aws_sdk_imagebuilder.types.log_group_name.LogGroupName"
    ]
    """<p>The log group name that Image Builder uses for the log output during creation of a new pipeline. If not specified, the pipeline log group name defaults to <code>/aws/imagebuilder/pipeline/pipeline-name</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineLoggingConfiguration) -> dict:
    out: dict = {}
    if "image_log_group_name" in value:
        out["imageLogGroupName"] = value["image_log_group_name"]
    if "pipeline_log_group_name" in value:
        out["pipelineLogGroupName"] = value["pipeline_log_group_name"]
    return out


def deserialize_json(data: dict) -> PipelineLoggingConfiguration:
    out: PipelineLoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "imageLogGroupName" in data:
        out["image_log_group_name"] = data["imageLogGroupName"]
    if "pipelineLogGroupName" in data:
        out["pipeline_log_group_name"] = data["pipelineLogGroupName"]
    return out
