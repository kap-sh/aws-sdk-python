"""Generated from Smithy shape ``com.amazonaws.datapipeline#PipelineObjectMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.pipeline_object

PipelineObjectMap: TypeAlias = dict[
    "capo_data_pipeline.types.id.id",
    "capo_data_pipeline.types.pipeline_object.PipelineObject",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PipelineObjectMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_data_pipeline.types.pipeline_object

        out[key] = capo_data_pipeline.types.pipeline_object.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineObjectMap:
    out: PipelineObjectMap = {}
    for key, value in data.items():
        import capo_data_pipeline.types.pipeline_object

        out[key] = capo_data_pipeline.types.pipeline_object.deserialize_aws_json_1_1(
            value
        )
    return out
