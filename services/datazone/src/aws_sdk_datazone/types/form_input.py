"""Generated from Smithy shape ``com.amazonaws.datazone#FormInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.form_name
    import aws_sdk_datazone.types.form_type_identifier
    import aws_sdk_datazone.types.revision_input


class FormInput(TypedDict):
    form_name: "aws_sdk_datazone.types.form_name.FormName"
    """<p>The name of the metadata form.</p>"""
    type_identifier: NotRequired[
        "aws_sdk_datazone.types.form_type_identifier.FormTypeIdentifier"
    ]
    """<p>The ID of the metadata form type.</p>"""
    type_revision: NotRequired["aws_sdk_datazone.types.revision_input.RevisionInput"]
    """<p>The revision of the metadata form type.</p>"""
    content: NotRequired["str"]
    """<p>The content of the metadata form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormInput) -> dict:
    out: dict = {}
    out["formName"] = value["form_name"]
    if "type_identifier" in value:
        out["typeIdentifier"] = value["type_identifier"]
    if "type_revision" in value:
        out["typeRevision"] = value["type_revision"]
    if "content" in value:
        out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> FormInput:
    out: FormInput = {}  # type: ignore[typeddict-item]
    if "formName" in data:
        out["form_name"] = data["formName"]
    else:
        raise DeserializationError("FormInput.form_name required")
    if "typeIdentifier" in data:
        out["type_identifier"] = data["typeIdentifier"]
    if "typeRevision" in data:
        out["type_revision"] = data["typeRevision"]
    if "content" in data:
        out["content"] = data["content"]
    return out
