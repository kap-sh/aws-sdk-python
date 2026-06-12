"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineExecutionFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.succeeded_in_stage_filter


class PipelineExecutionFilter(TypedDict):
    succeeded_in_stage: NotRequired[
        "aws_sdk_codepipeline.types.succeeded_in_stage_filter.SucceededInStageFilter"
    ]
    """<p>Filter for pipeline executions where the stage was successful in the current pipeline version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineExecutionFilter) -> dict:
    out: dict = {}
    if "succeeded_in_stage" in value:
        import aws_sdk_codepipeline.types.succeeded_in_stage_filter

        out["succeededInStage"] = (
            aws_sdk_codepipeline.types.succeeded_in_stage_filter.serialize_aws_json_1_1(
                value["succeeded_in_stage"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineExecutionFilter:
    out: PipelineExecutionFilter = {}  # type: ignore[typeddict-item]
    if "succeededInStage" in data:
        import aws_sdk_codepipeline.types.succeeded_in_stage_filter

        out["succeeded_in_stage"] = (
            aws_sdk_codepipeline.types.succeeded_in_stage_filter.deserialize_aws_json_1_1(
                data["succeededInStage"]
            )
        )
    return out
