"""Generated from Smithy shape ``com.amazonaws.fis#StartExperimentExperimentOptionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.actions_mode


class StartExperimentExperimentOptionsInput(TypedDict, closed=True):
    actions_mode: NotRequired["capo_fis.types.actions_mode.ActionsMode"]
    """<p>Specifies the actions mode for experiment options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartExperimentExperimentOptionsInput) -> dict:
    out: dict = {}
    if "actions_mode" in value:
        import capo_fis.types.actions_mode

        out["actionsMode"] = capo_fis.types.actions_mode.serialize_json(
            value["actions_mode"]
        )
    return out


def deserialize_json(data: dict) -> StartExperimentExperimentOptionsInput:
    out: StartExperimentExperimentOptionsInput = {}  # type: ignore[typeddict-item]
    if "actionsMode" in data:
        import capo_fis.types.actions_mode

        out["actions_mode"] = capo_fis.types.actions_mode.deserialize_json(
            data["actionsMode"]
        )
    return out
