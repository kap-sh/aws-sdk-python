"""Generated from Smithy shape ``com.amazonaws.medialive#RestartChannelPipelinesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_channel_pipeline_id_to_restart
    import aws_sdk_medialive.types.__string


class RestartChannelPipelinesRequest(TypedDict, closed=True):
    channel_id: "aws_sdk_medialive.types.__string.__string"
    """ID of channel"""
    pipeline_ids: NotRequired[
        "aws_sdk_medialive.types.__list_of_channel_pipeline_id_to_restart.__listOfChannelPipelineIdToRestart"
    ]
    """An array of pipelines to restart in this channel. Format PIPELINE_0 or PIPELINE_1."""


# --- restJson1 ser/de ---
def serialize_json(value: RestartChannelPipelinesRequest) -> dict:
    out: dict = {}
    if "pipeline_ids" in value:
        import aws_sdk_medialive.types.__list_of_channel_pipeline_id_to_restart

        out["pipelineIds"] = (
            aws_sdk_medialive.types.__list_of_channel_pipeline_id_to_restart.serialize_json(
                value["pipeline_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> RestartChannelPipelinesRequest:
    out: RestartChannelPipelinesRequest = {}  # type: ignore[typeddict-item]
    if "pipelineIds" in data:
        import aws_sdk_medialive.types.__list_of_channel_pipeline_id_to_restart

        out["pipeline_ids"] = (
            aws_sdk_medialive.types.__list_of_channel_pipeline_id_to_restart.deserialize_json(
                data["pipelineIds"]
            )
        )
    return out
