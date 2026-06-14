"""Generated from Smithy shape ``com.amazonaws.datazone#FormEntryOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.form_type_name
    import aws_sdk_datazone.types.revision


class FormEntryOutput(TypedDict):
    type_name: "aws_sdk_datazone.types.form_type_name.FormTypeName"
    """<p>The name of the type of the form entry.</p>"""
    type_revision: "aws_sdk_datazone.types.revision.Revision"
    """<p>The type revision of the form entry.</p>"""
    required: NotRequired["bool"]
    """<p>Specifies whether a form entry is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormEntryOutput) -> dict:
    out: dict = {}
    out["typeName"] = value["type_name"]
    out["typeRevision"] = value["type_revision"]
    if "required" in value:
        out["required"] = value["required"]
    return out


def deserialize_json(data: dict) -> FormEntryOutput:
    out: FormEntryOutput = {}  # type: ignore[typeddict-item]
    if "typeName" in data:
        out["type_name"] = data["typeName"]
    else:
        raise DeserializationError("FormEntryOutput.type_name required")
    if "typeRevision" in data:
        out["type_revision"] = data["typeRevision"]
    else:
        raise DeserializationError("FormEntryOutput.type_revision required")
    if "required" in data:
        out["required"] = data["required"]
    return out
