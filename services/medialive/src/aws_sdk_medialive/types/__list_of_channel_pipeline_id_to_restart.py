"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfChannelPipelineIdToRestart``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.channel_pipeline_id_to_restart

__listOfChannelPipelineIdToRestart: TypeAlias = list[
    "aws_sdk_medialive.types.channel_pipeline_id_to_restart.ChannelPipelineIdToRestart"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfChannelPipelineIdToRestart) -> list:
    import aws_sdk_medialive.types.channel_pipeline_id_to_restart

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.channel_pipeline_id_to_restart.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfChannelPipelineIdToRestart:
    import aws_sdk_medialive.types.channel_pipeline_id_to_restart

    out: __listOfChannelPipelineIdToRestart = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.channel_pipeline_id_to_restart.deserialize_json(
                item
            )
        )
    return out
