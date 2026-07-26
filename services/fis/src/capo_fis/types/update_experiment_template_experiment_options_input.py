"""Generated from Smithy shape ``com.amazonaws.fis#UpdateExperimentTemplateExperimentOptionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.empty_target_resolution_mode


class UpdateExperimentTemplateExperimentOptionsInput(TypedDict, closed=True):
    empty_target_resolution_mode: NotRequired[
        "capo_fis.types.empty_target_resolution_mode.EmptyTargetResolutionMode"
    ]
    """<p>The empty target resolution mode of the experiment template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateExperimentTemplateExperimentOptionsInput) -> dict:
    out: dict = {}
    if "empty_target_resolution_mode" in value:
        import capo_fis.types.empty_target_resolution_mode

        out["emptyTargetResolutionMode"] = (
            capo_fis.types.empty_target_resolution_mode.serialize_json(
                value["empty_target_resolution_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateExperimentTemplateExperimentOptionsInput:
    out: UpdateExperimentTemplateExperimentOptionsInput = {}  # type: ignore[typeddict-item]
    if "emptyTargetResolutionMode" in data:
        import capo_fis.types.empty_target_resolution_mode

        out["empty_target_resolution_mode"] = (
            capo_fis.types.empty_target_resolution_mode.deserialize_json(
                data["emptyTargetResolutionMode"]
            )
        )
    return out
