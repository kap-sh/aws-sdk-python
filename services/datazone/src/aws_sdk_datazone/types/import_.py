"""Generated from Smithy shape ``com.amazonaws.datazone#Import``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.form_type_name
    import aws_sdk_datazone.types.revision


class Import(TypedDict, closed=True):
    name: "aws_sdk_datazone.types.form_type_name.FormTypeName"
    """<p>The name of the import.</p>"""
    revision: "aws_sdk_datazone.types.revision.Revision"
    """<p>The revision of the import.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Import) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["revision"] = value["revision"]
    return out


def deserialize_json(data: dict) -> Import:
    out: Import = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Import.name required")
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        raise DeserializationError("Import.revision required")
    return out
