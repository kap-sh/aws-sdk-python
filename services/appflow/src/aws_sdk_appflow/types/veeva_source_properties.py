"""Generated from Smithy shape ``com.amazonaws.appflow#VeevaSourceProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.boolean
    import aws_sdk_appflow.types.document_type
    import aws_sdk_appflow.types.object


class VeevaSourceProperties(TypedDict):
    object: "aws_sdk_appflow.types.object.Object"
    """<p> The object specified in the Veeva flow source. </p>"""
    document_type: NotRequired["aws_sdk_appflow.types.document_type.DocumentType"]
    """<p>The document type specified in the Veeva document extract flow.</p>"""
    include_source_files: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Boolean value to include source files in Veeva document extract flow.</p>"""
    include_renditions: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Boolean value to include file renditions in Veeva document extract flow.</p>"""
    include_all_versions: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Boolean value to include All Versions of files in Veeva document extract flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VeevaSourceProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    if "document_type" in value:
        out["documentType"] = value["document_type"]
    out["includeSourceFiles"] = value.get("include_source_files", False)
    out["includeRenditions"] = value.get("include_renditions", False)
    out["includeAllVersions"] = value.get("include_all_versions", False)
    return out


def deserialize_json(data: dict) -> VeevaSourceProperties:
    out: VeevaSourceProperties = {}  # type: ignore[typeddict-item]
    if "object" in data:
        out["object"] = data["object"]
    else:
        raise DeserializationError("VeevaSourceProperties.object required")
    if "documentType" in data:
        out["document_type"] = data["documentType"]
    if "includeSourceFiles" in data:
        out["include_source_files"] = data["includeSourceFiles"]
    else:
        out["include_source_files"] = False
    if "includeRenditions" in data:
        out["include_renditions"] = data["includeRenditions"]
    else:
        out["include_renditions"] = False
    if "includeAllVersions" in data:
        out["include_all_versions"] = data["includeAllVersions"]
    else:
        out["include_all_versions"] = False
    return out
