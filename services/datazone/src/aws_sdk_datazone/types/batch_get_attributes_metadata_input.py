"""Generated from Smithy shape ``com.amazonaws.datazone#BatchGetAttributesMetadataInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_datazone.types.attribute_entity_type
    import aws_sdk_datazone.types.attributes_list
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.entity_id
    import aws_sdk_datazone.types.revision

class BatchGetAttributesMetadataInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The domain ID where you want to get the attribute metadata.</p>"""
    entity_type: "aws_sdk_datazone.types.attribute_entity_type.AttributeEntityType"
    """<p>The entity type for which you want to get attribute metadata.</p>"""
    entity_identifier: "aws_sdk_datazone.types.entity_id.EntityId"
    """<p>The entity ID for which you want to get attribute metadata.</p>"""
    entity_revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The entity revision for which you want to get attribute metadata.</p>"""
    attribute_identifiers: "aws_sdk_datazone.types.attributes_list.AttributesList"
    """<p>The attribute identifier.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAttributesMetadataInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> BatchGetAttributesMetadataInput:
    out: BatchGetAttributesMetadataInput = {}  # type: ignore[typeddict-item]
    return out