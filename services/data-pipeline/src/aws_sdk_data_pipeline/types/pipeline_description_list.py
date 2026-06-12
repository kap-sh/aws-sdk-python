"""Generated from Smithy shape ``com.amazonaws.datapipeline#PipelineDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.pipeline_description

PipelineDescriptionList: TypeAlias = list[
    "aws_sdk_data_pipeline.types.pipeline_description.PipelineDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineDescriptionList) -> list:
    import aws_sdk_data_pipeline.types.pipeline_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_data_pipeline.types.pipeline_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PipelineDescriptionList:
    import aws_sdk_data_pipeline.types.pipeline_description

    out: PipelineDescriptionList = []
    for item in data:
        out.append(
            aws_sdk_data_pipeline.types.pipeline_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
