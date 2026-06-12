"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DeleteJobTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.resource_id_string


class DeleteJobTemplateResponse(TypedDict):
    id: NotRequired["aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>This output contains the ID of the job template that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteJobTemplateResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> DeleteJobTemplateResponse:
    out: DeleteJobTemplateResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    return out
