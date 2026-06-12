"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfPipelineDetail``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.pipeline_detail

__listOfPipelineDetail: TypeAlias = list[
    "aws_sdk_medialive.types.pipeline_detail.PipelineDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPipelineDetail) -> list:
    import aws_sdk_medialive.types.pipeline_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.pipeline_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfPipelineDetail:
    import aws_sdk_medialive.types.pipeline_detail

    out: __listOfPipelineDetail = []
    for item in data:
        out.append(aws_sdk_medialive.types.pipeline_detail.deserialize_json(item))
    return out
