"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataFormSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.form_name
    import aws_sdk_datazone.types.form_type_name
    import aws_sdk_datazone.types.revision


class MetadataFormSummary(TypedDict, closed=True):
    form_name: NotRequired["aws_sdk_datazone.types.form_name.FormName"]
    """<p>The form name of the metadata form.</p>"""
    type_name: "aws_sdk_datazone.types.form_type_name.FormTypeName"
    """<p>The type name of the metadata form.</p>"""
    type_revision: "aws_sdk_datazone.types.revision.Revision"
    """<p>The type revision of the metadata form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataFormSummary) -> dict:
    out: dict = {}
    if "form_name" in value:
        out["formName"] = value["form_name"]
    out["typeName"] = value["type_name"]
    out["typeRevision"] = value["type_revision"]
    return out


def deserialize_json(data: dict) -> MetadataFormSummary:
    out: MetadataFormSummary = {}  # type: ignore[typeddict-item]
    if "formName" in data:
        out["form_name"] = data["formName"]
    if "typeName" in data:
        out["type_name"] = data["typeName"]
    else:
        raise DeserializationError("MetadataFormSummary.type_name required")
    if "typeRevision" in data:
        out["type_revision"] = data["typeRevision"]
    else:
        raise DeserializationError("MetadataFormSummary.type_revision required")
    return out
