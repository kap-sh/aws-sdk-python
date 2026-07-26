"""Generated from Smithy shape ``com.amazonaws.datazone#BatchGetAttributesMetadataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.attribute_entity_type
    import capo_datazone.types.attributes_list
    import capo_datazone.types.domain_id
    import capo_datazone.types.entity_id
    import capo_datazone.types.revision


class BatchGetAttributesMetadataInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The domain ID where you want to get the attribute metadata.</p>"""
    entity_type: "capo_datazone.types.attribute_entity_type.AttributeEntityType"
    """<p>The entity type for which you want to get attribute metadata.</p>"""
    entity_identifier: "capo_datazone.types.entity_id.EntityId"
    """<p>The entity ID for which you want to get attribute metadata.</p>"""
    entity_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The entity revision for which you want to get attribute metadata.</p>"""
    attribute_identifiers: "capo_datazone.types.attributes_list.AttributesList"
    """<p>The attribute identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAttributesMetadataInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> BatchGetAttributesMetadataInput:
    out: BatchGetAttributesMetadataInput = {}  # type: ignore[typeddict-item]
    return out
