"""Generated from Smithy shape ``com.amazonaws.fis#StartExperimentExperimentOptionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.actions_mode


class StartExperimentExperimentOptionsInput(TypedDict):
    actions_mode: NotRequired["aws_sdk_fis.types.actions_mode.ActionsMode"]
    """<p>Specifies the actions mode for experiment options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartExperimentExperimentOptionsInput) -> dict:
    out: dict = {}
    if "actions_mode" in value:
        import aws_sdk_fis.types.actions_mode

        out["actionsMode"] = aws_sdk_fis.types.actions_mode.serialize_json(
            value["actions_mode"]
        )
    return out


def deserialize_json(data: dict) -> StartExperimentExperimentOptionsInput:
    out: StartExperimentExperimentOptionsInput = {}  # type: ignore[typeddict-item]
    if "actionsMode" in data:
        import aws_sdk_fis.types.actions_mode

        out["actions_mode"] = aws_sdk_fis.types.actions_mode.deserialize_json(
            data["actionsMode"]
        )
    return out
