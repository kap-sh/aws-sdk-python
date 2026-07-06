"""Generated from Smithy shape ``com.amazonaws.fis#GetExperimentTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template


class GetExperimentTemplateResponse(TypedDict, closed=True):
    experiment_template: NotRequired[
        "aws_sdk_fis.types.experiment_template.ExperimentTemplate"
    ]
    """<p>Information about the experiment template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExperimentTemplateResponse) -> dict:
    out: dict = {}
    if "experiment_template" in value:
        import aws_sdk_fis.types.experiment_template

        out["experimentTemplate"] = (
            aws_sdk_fis.types.experiment_template.serialize_json(
                value["experiment_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetExperimentTemplateResponse:
    out: GetExperimentTemplateResponse = {}  # type: ignore[typeddict-item]
    if "experimentTemplate" in data:
        import aws_sdk_fis.types.experiment_template

        out["experiment_template"] = (
            aws_sdk_fis.types.experiment_template.deserialize_json(
                data["experimentTemplate"]
            )
        )
    return out
