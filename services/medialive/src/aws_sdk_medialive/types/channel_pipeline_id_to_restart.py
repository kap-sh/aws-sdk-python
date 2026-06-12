"""Generated from Smithy shape ``com.amazonaws.medialive#ChannelPipelineIdToRestart``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Property of RestartChannelPipelinesRequest"""
ChannelPipelineIdToRestart: TypeAlias = Literal[
    "PIPELINE_0",
    "PIPELINE_1",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PIPELINE_0",
        "PIPELINE_1",
    )
)


def serialize_json(value: ChannelPipelineIdToRestart) -> str:
    return value


def deserialize_json(data: str) -> ChannelPipelineIdToRestart:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ChannelPipelineIdToRestart value: {data!r}"
        )
    return cast(ChannelPipelineIdToRestart, data)
