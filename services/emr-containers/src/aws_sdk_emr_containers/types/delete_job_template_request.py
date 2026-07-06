"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DeleteJobTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.resource_id_string


class DeleteJobTemplateRequest(TypedDict, closed=True):
    id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    """<p>The ID of the job template that will be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteJobTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteJobTemplateRequest:
    out: DeleteJobTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
