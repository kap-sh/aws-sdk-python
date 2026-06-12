"""Generated from Smithy shape ``com.amazonaws.osis#PipelineDestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_destination

PipelineDestinationList: TypeAlias = list[
    "aws_sdk_osis.types.pipeline_destination.PipelineDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: PipelineDestinationList) -> list:
    import aws_sdk_osis.types.pipeline_destination

    out: list = []
    for item in value:
        out.append(aws_sdk_osis.types.pipeline_destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> PipelineDestinationList:
    import aws_sdk_osis.types.pipeline_destination

    out: PipelineDestinationList = []
    for item in data:
        out.append(aws_sdk_osis.types.pipeline_destination.deserialize_json(item))
    return out
