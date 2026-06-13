"""Generated from Smithy shape ``com.amazonaws.datazone#CreateFormTypeInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.form_type_name
    import aws_sdk_datazone.types.form_type_status
    import aws_sdk_datazone.types.model
    import aws_sdk_datazone.types.project_id


class CreateFormTypeInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this metadata form type is created.</p>"""
    name: "aws_sdk_datazone.types.form_type_name.FormTypeName"
    """<p>The name of this Amazon DataZone metadata form type.</p>"""
    model: "aws_sdk_datazone.types.model.Model"
    """<p>The model of this Amazon DataZone metadata form type.</p>"""
    owning_project_identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The ID of the Amazon DataZone project that owns this metadata form type.</p>"""
    status: NotRequired["aws_sdk_datazone.types.form_type_status.FormTypeStatus"]
    """<p>The status of this Amazon DataZone metadata form type.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of this Amazon DataZone metadata form type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFormTypeInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_datazone.types.model

    out["model"] = aws_sdk_datazone.types.model.serialize_json(value["model"])
    out["owningProjectIdentifier"] = value["owning_project_identifier"]
    if "status" in value:
        import aws_sdk_datazone.types.form_type_status

        out["status"] = aws_sdk_datazone.types.form_type_status.serialize_json(
            value["status"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> CreateFormTypeInput:
    out: CreateFormTypeInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateFormTypeInput.name required")
    if "model" in data:
        import aws_sdk_datazone.types.model

        out["model"] = aws_sdk_datazone.types.model.deserialize_json(data["model"])
    else:
        raise DeserializationError("CreateFormTypeInput.model required")
    if "owningProjectIdentifier" in data:
        out["owning_project_identifier"] = data["owningProjectIdentifier"]
    else:
        raise DeserializationError(
            "CreateFormTypeInput.owning_project_identifier required"
        )
    if "status" in data:
        import aws_sdk_datazone.types.form_type_status

        out["status"] = aws_sdk_datazone.types.form_type_status.deserialize_json(
            data["status"]
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
