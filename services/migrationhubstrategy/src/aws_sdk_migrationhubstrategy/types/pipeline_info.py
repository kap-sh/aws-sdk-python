"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#PipelineInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.pipeline_type
    import aws_sdk_migrationhubstrategy.types.string


class PipelineInfo(TypedDict):
    pipeline_type: NotRequired[
        "aws_sdk_migrationhubstrategy.types.pipeline_type.PipelineType"
    ]
    """<p>The type of pipeline.</p>"""
    pipeline_configuration_time_stamp: NotRequired[
        "aws_sdk_migrationhubstrategy.types.string.String"
    ]
    """<p>The time when the pipeline info was configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineInfo) -> dict:
    out: dict = {}
    if "pipeline_type" in value:
        out["pipelineType"] = value["pipeline_type"]
    if "pipeline_configuration_time_stamp" in value:
        out["pipelineConfigurationTimeStamp"] = value[
            "pipeline_configuration_time_stamp"
        ]
    return out


def deserialize_json(data: dict) -> PipelineInfo:
    out: PipelineInfo = {}  # type: ignore[typeddict-item]
    if "pipelineType" in data:
        out["pipeline_type"] = data["pipelineType"]
    if "pipelineConfigurationTimeStamp" in data:
        out["pipeline_configuration_time_stamp"] = data[
            "pipelineConfigurationTimeStamp"
        ]
    return out
