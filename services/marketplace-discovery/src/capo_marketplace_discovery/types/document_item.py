"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DocumentItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.legal_document_type
    import capo_marketplace_discovery.types.url


class DocumentItem(TypedDict, closed=True):
    type: "capo_marketplace_discovery.types.legal_document_type.LegalDocumentType"
    """<p>The category of the legal document, such as <code>StandardEula</code> or <code>CustomEula</code>.</p>"""
    url: "capo_marketplace_discovery.types.url.URL"
    """<p>The URL where the legal document can be accessed.</p>"""
    version: NotRequired["str"]
    """<p>The version of the standard contract, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentItem) -> dict:
    out: dict = {}
    import capo_marketplace_discovery.types.legal_document_type

    out["type"] = capo_marketplace_discovery.types.legal_document_type.serialize_json(
        value["type"]
    )
    out["url"] = value["url"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> DocumentItem:
    out: DocumentItem = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import capo_marketplace_discovery.types.legal_document_type

        out["type"] = (
            capo_marketplace_discovery.types.legal_document_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("DocumentItem.type required")
    if "url" in data:
        out["url"] = data["url"]
    else:
        raise DeserializationError("DocumentItem.url required")
    if "version" in data:
        out["version"] = data["version"]
    return out
