"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribePipelineDefinitionForExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.pipeline_definition
    import capo_sagemaker.types.timestamp


class DescribePipelineDefinitionForExecutionResponse(TypedDict, closed=True):
    pipeline_definition: NotRequired[
        "capo_sagemaker.types.pipeline_definition.PipelineDefinition"
    ]
    """<p>The JSON pipeline definition.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the pipeline was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribePipelineDefinitionForExecutionResponse,
) -> dict:
    out: dict = {}
    if "pipeline_definition" in value:
        out["PipelineDefinition"] = value["pipeline_definition"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribePipelineDefinitionForExecutionResponse:
    out: DescribePipelineDefinitionForExecutionResponse = {}  # type: ignore[typeddict-item]
    if "PipelineDefinition" in data:
        out["pipeline_definition"] = data["PipelineDefinition"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
