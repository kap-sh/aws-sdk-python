"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.attribute_type
    import aws_sdk_qbusiness.types.document_metadata_configuration_name
    import aws_sdk_qbusiness.types.status


class DocumentAttributeConfiguration(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_qbusiness.types.document_metadata_configuration_name.DocumentMetadataConfigurationName"
    ]
    """<p>The name of the document attribute.</p>"""
    type: NotRequired["aws_sdk_qbusiness.types.attribute_type.AttributeType"]
    """<p>The type of document attribute.</p>"""
    search: NotRequired["aws_sdk_qbusiness.types.status.Status"]
    """<p>Information about whether the document attribute can be used by an end user to search for information on their web experience.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttributeConfiguration) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import aws_sdk_qbusiness.types.attribute_type

        out["type"] = aws_sdk_qbusiness.types.attribute_type.serialize_json(
            value["type"]
        )
    if "search" in value:
        import aws_sdk_qbusiness.types.status

        out["search"] = aws_sdk_qbusiness.types.status.serialize_json(value["search"])
    return out


def deserialize_json(data: dict) -> DocumentAttributeConfiguration:
    out: DocumentAttributeConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import aws_sdk_qbusiness.types.attribute_type

        out["type"] = aws_sdk_qbusiness.types.attribute_type.deserialize_json(
            data["type"]
        )
    if "search" in data:
        import aws_sdk_qbusiness.types.status

        out["search"] = aws_sdk_qbusiness.types.status.deserialize_json(data["search"])
    return out
