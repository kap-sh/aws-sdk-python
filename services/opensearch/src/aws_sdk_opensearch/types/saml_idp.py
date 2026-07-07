"""Generated from Smithy shape ``com.amazonaws.opensearch#SAMLIdp``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.saml_entity_id
    import aws_sdk_opensearch.types.saml_metadata


class SAMLIdp(TypedDict, closed=True):
    metadata_content: "aws_sdk_opensearch.types.saml_metadata.SAMLMetadata"
    """<p>The metadata of the SAML application, in XML format.</p>"""
    entity_id: "aws_sdk_opensearch.types.saml_entity_id.SAMLEntityId"
    """<p>The unique entity ID of the application in the SAML identity provider.</p>"""


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
