"""Generated from Smithy shape ``com.amazonaws.datazone#FormOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.form_name
    import aws_sdk_datazone.types.form_type_name
    import aws_sdk_datazone.types.revision


class FormOutput(TypedDict):
    form_name: "aws_sdk_datazone.types.form_name.FormName"
    """<p>The name of the metadata form.</p>"""
    type_name: NotRequired["aws_sdk_datazone.types.form_type_name.FormTypeName"]
    """<p>The name of the metadata form type.</p>"""
    type_revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of the metadata form type.</p>"""
    content: NotRequired["str"]
    """<p>The content of the metadata form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormOutput) -> dict:
    out: dict = {}
    out["formName"] = value["form_name"]
    if "type_name" in value:
        out["typeName"] = value["type_name"]
    if "type_revision" in value:
        out["typeRevision"] = value["type_revision"]
    if "content" in value:
        out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> FormOutput:
    out: FormOutput = {}  # type: ignore[typeddict-item]
    if "formName" in data:
        out["form_name"] = data["formName"]
    else:
        raise DeserializationError("FormOutput.form_name required")
    if "typeName" in data:
        out["type_name"] = data["typeName"]
    if "typeRevision" in data:
        out["type_revision"] = data["typeRevision"]
    if "content" in data:
        out["content"] = data["content"]
    return out
