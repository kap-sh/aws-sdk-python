"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataFormReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.form_type_identifier
    import aws_sdk_datazone.types.revision


class MetadataFormReference(TypedDict, closed=True):
    type_identifier: "aws_sdk_datazone.types.form_type_identifier.FormTypeIdentifier"
    """<p>The type ID of the metadata form reference.</p>"""
    type_revision: "aws_sdk_datazone.types.revision.Revision"
    """<p>The type revision of the metadata form reference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataFormReference) -> dict:
    out: dict = {}
    out["typeIdentifier"] = value["type_identifier"]
    out["typeRevision"] = value["type_revision"]
    return out


def deserialize_json(data: dict) -> MetadataFormReference:
    out: MetadataFormReference = {}  # type: ignore[typeddict-item]
    if "typeIdentifier" in data:
        out["type_identifier"] = data["typeIdentifier"]
    else:
        raise DeserializationError("MetadataFormReference.type_identifier required")
    if "typeRevision" in data:
        out["type_revision"] = data["typeRevision"]
    else:
        raise DeserializationError("MetadataFormReference.type_revision required")
    return out
