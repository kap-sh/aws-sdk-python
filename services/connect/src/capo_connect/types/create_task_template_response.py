"""Generated from Smithy shape ``com.amazonaws.connect#CreateTaskTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.task_template_arn
    import capo_connect.types.task_template_id


class CreateTaskTemplateResponse(TypedDict, closed=True):
    id: "capo_connect.types.task_template_id.TaskTemplateId"
    """<p>The identifier of the task template resource.</p>"""
    arn: "capo_connect.types.task_template_arn.TaskTemplateArn"
    """<p>The Amazon Resource Name (ARN) for the task template resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTaskTemplateResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateTaskTemplateResponse:
    out: CreateTaskTemplateResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("CreateTaskTemplateResponse.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("CreateTaskTemplateResponse.arn required")
    return out
