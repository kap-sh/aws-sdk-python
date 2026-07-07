"""Generated from Smithy shape ``com.amazonaws.fis#DeleteExperimentTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_id


class DeleteExperimentTemplateRequest(TypedDict, closed=True):
    id: "aws_sdk_fis.types.experiment_template_id.ExperimentTemplateId"
    """<p>The ID of the experiment template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteExperimentTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteExperimentTemplateRequest:
    out: DeleteExperimentTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
