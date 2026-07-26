"""Generated from Smithy shape ``com.amazonaws.datapipeline#pipelineList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_data_pipeline.types.pipeline_id_name

pipelineList: TypeAlias = list[
    "capo_data_pipeline.types.pipeline_id_name.PipelineIdName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: pipelineList) -> list:
    import capo_data_pipeline.types.pipeline_id_name

    out: list = []
    for item in value:
        out.append(
            capo_data_pipeline.types.pipeline_id_name.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> pipelineList:
    import capo_data_pipeline.types.pipeline_id_name

    out: pipelineList = []
    for item in data:
        out.append(
            capo_data_pipeline.types.pipeline_id_name.deserialize_aws_json_1_1(item)
        )
    return out
