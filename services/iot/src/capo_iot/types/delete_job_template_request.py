"""Generated from Smithy shape ``com.amazonaws.iot#DeleteJobTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.job_template_id


class DeleteJobTemplateRequest(TypedDict, closed=True):
    job_template_id: "capo_iot.types.job_template_id.JobTemplateId"
    """<p>The unique identifier of the job template to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteJobTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteJobTemplateRequest:
    out: DeleteJobTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
