"""Generated from Smithy shape ``com.amazonaws.medialive#PauseStateScheduleActionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_pipeline_pause_state_settings


class PauseStateScheduleActionSettings(TypedDict, closed=True):
    pipelines: NotRequired[
        "capo_medialive.types.__list_of_pipeline_pause_state_settings.__listOfPipelinePauseStateSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PauseStateScheduleActionSettings) -> dict:
    out: dict = {}
    if "pipelines" in value:
        import capo_medialive.types.__list_of_pipeline_pause_state_settings

        out["pipelines"] = (
            capo_medialive.types.__list_of_pipeline_pause_state_settings.serialize_json(
                value["pipelines"]
            )
        )
    return out


def deserialize_json(data: dict) -> PauseStateScheduleActionSettings:
    out: PauseStateScheduleActionSettings = {}  # type: ignore[typeddict-item]
    if "pipelines" in data:
        import capo_medialive.types.__list_of_pipeline_pause_state_settings

        out["pipelines"] = (
            capo_medialive.types.__list_of_pipeline_pause_state_settings.deserialize_json(
                data["pipelines"]
            )
        )
    return out
