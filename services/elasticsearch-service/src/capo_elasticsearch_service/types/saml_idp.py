"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#SAMLIdp``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.saml_entity_id
    import capo_elasticsearch_service.types.saml_metadata


class SAMLIdp(TypedDict, closed=True):
    metadata_content: "capo_elasticsearch_service.types.saml_metadata.SAMLMetadata"
    """<p>The Metadata of the SAML application in xml format.</p>"""
    entity_id: "capo_elasticsearch_service.types.saml_entity_id.SAMLEntityId"
    """<p>The unique Entity ID of the application in SAML Identity Provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SAMLIdp) -> dict:
    out: dict = {}
    out["MetadataContent"] = value["metadata_content"]
    out["EntityId"] = value["entity_id"]
    return out


def deserialize_json(data: dict) -> SAMLIdp:
    out: SAMLIdp = {}  # type: ignore[typeddict-item]
    if "MetadataContent" in data:
        out["metadata_content"] = data["MetadataContent"]
    else:
        raise DeserializationError("SAMLIdp.metadata_content required")
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    else:
        raise DeserializationError("SAMLIdp.entity_id required")
    return out
