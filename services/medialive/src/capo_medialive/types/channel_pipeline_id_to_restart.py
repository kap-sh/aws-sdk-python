"""Generated from Smithy shape ``com.amazonaws.medialive#ChannelPipelineIdToRestart``."""

from typing import Literal, TypeAlias, cast

"""Property of RestartChannelPipelinesRequest"""
ChannelPipelineIdToRestart: TypeAlias = Literal[
    "PIPELINE_0",
    "PIPELINE_1",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelPipelineIdToRestart) -> str:
    return value


def deserialize_json(data: str) -> ChannelPipelineIdToRestart:
    return cast(ChannelPipelineIdToRestart, data)
