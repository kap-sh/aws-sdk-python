"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfPipelinePauseStateSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.pipeline_pause_state_settings

__listOfPipelinePauseStateSettings: TypeAlias = list[
    "capo_medialive.types.pipeline_pause_state_settings.PipelinePauseStateSettings"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPipelinePauseStateSettings) -> list:
    import capo_medialive.types.pipeline_pause_state_settings

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.pipeline_pause_state_settings.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfPipelinePauseStateSettings:
    import capo_medialive.types.pipeline_pause_state_settings

    out: __listOfPipelinePauseStateSettings = []
    for item in data:
        out.append(
            capo_medialive.types.pipeline_pause_state_settings.deserialize_json(item)
        )
    return out
