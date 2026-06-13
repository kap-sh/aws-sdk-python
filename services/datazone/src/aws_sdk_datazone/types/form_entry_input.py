"""Generated from Smithy shape ``com.amazonaws.datazone#FormEntryInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.form_type_identifier
    import aws_sdk_datazone.types.revision


class FormEntryInput(TypedDict):
    type_identifier: "aws_sdk_datazone.types.form_type_identifier.FormTypeIdentifier"
    """<p>The type ID of the form entry.</p>"""
    type_revision: "aws_sdk_datazone.types.revision.Revision"
    """<p>The type revision of the form entry.</p>"""
    required: NotRequired["bool"]
    """<p>Specifies whether a form entry is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormEntryInput) -> dict:
    out: dict = {}
    out["typeIdentifier"] = value["type_identifier"]
    out["typeRevision"] = value["type_revision"]
    if "required" in value:
        out["required"] = value["required"]
    return out


def deserialize_json(data: dict) -> FormEntryInput:
    out: FormEntryInput = {}  # type: ignore[typeddict-item]
    if "typeIdentifier" in data:
        out["type_identifier"] = data["typeIdentifier"]
    else:
        raise DeserializationError("FormEntryInput.type_identifier required")
    if "typeRevision" in data:
        out["type_revision"] = data["typeRevision"]
    else:
        raise DeserializationError("FormEntryInput.type_revision required")
    if "required" in data:
        out["required"] = data["required"]
    return out
