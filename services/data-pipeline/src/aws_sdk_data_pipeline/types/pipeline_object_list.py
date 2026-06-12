"""Generated from Smithy shape ``com.amazonaws.datapipeline#PipelineObjectList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.pipeline_object

PipelineObjectList: TypeAlias = list[
    "aws_sdk_data_pipeline.types.pipeline_object.PipelineObject"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineObjectList) -> list:
    import aws_sdk_data_pipeline.types.pipeline_object

    out: list = []
    for item in value:
        out.append(
            aws_sdk_data_pipeline.types.pipeline_object.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PipelineObjectList:
    import aws_sdk_data_pipeline.types.pipeline_object

    out: PipelineObjectList = []
    for item in data:
        out.append(
            aws_sdk_data_pipeline.types.pipeline_object.deserialize_aws_json_1_1(item)
        )
    return out
