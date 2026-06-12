"""Generated from Smithy shape ``com.amazonaws.fis#UpdateExperimentTemplateExperimentOptionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.empty_target_resolution_mode


class UpdateExperimentTemplateExperimentOptionsInput(TypedDict):
    empty_target_resolution_mode: NotRequired[
        "aws_sdk_fis.types.empty_target_resolution_mode.EmptyTargetResolutionMode"
    ]
    """<p>The empty target resolution mode of the experiment template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateExperimentTemplateExperimentOptionsInput) -> dict:
    out: dict = {}
    if "empty_target_resolution_mode" in value:
        import aws_sdk_fis.types.empty_target_resolution_mode

        out["emptyTargetResolutionMode"] = (
            aws_sdk_fis.types.empty_target_resolution_mode.serialize_json(
                value["empty_target_resolution_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateExperimentTemplateExperimentOptionsInput:
    out: UpdateExperimentTemplateExperimentOptionsInput = {}  # type: ignore[typeddict-item]
    if "emptyTargetResolutionMode" in data:
        import aws_sdk_fis.types.empty_target_resolution_mode

        out["empty_target_resolution_mode"] = (
            aws_sdk_fis.types.empty_target_resolution_mode.deserialize_json(
                data["emptyTargetResolutionMode"]
            )
        )
    return out
