"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.attribute_type
    import capo_qbusiness.types.document_metadata_configuration_name
    import capo_qbusiness.types.status


class DocumentAttributeConfiguration(TypedDict, closed=True):
    name: NotRequired[
        "capo_qbusiness.types.document_metadata_configuration_name.DocumentMetadataConfigurationName"
    ]
    """<p>The name of the document attribute.</p>"""
    type: NotRequired["capo_qbusiness.types.attribute_type.AttributeType"]
    """<p>The type of document attribute.</p>"""
    search: NotRequired["capo_qbusiness.types.status.Status"]
    """<p>Information about whether the document attribute can be used by an end user to search for information on their web experience.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttributeConfiguration) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import capo_qbusiness.types.attribute_type

        out["type"] = capo_qbusiness.types.attribute_type.serialize_json(value["type"])
    if "search" in value:
        import capo_qbusiness.types.status

        out["search"] = capo_qbusiness.types.status.serialize_json(value["search"])
    return out


def deserialize_json(data: dict) -> DocumentAttributeConfiguration:
    out: DocumentAttributeConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import capo_qbusiness.types.attribute_type

        out["type"] = capo_qbusiness.types.attribute_type.deserialize_json(data["type"])
    if "search" in data:
        import capo_qbusiness.types.status

        out["search"] = capo_qbusiness.types.status.deserialize_json(data["search"])
    return out
