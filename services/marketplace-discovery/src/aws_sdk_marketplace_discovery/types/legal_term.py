"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#LegalTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.document_list
    import aws_sdk_marketplace_discovery.types.term_id
    import aws_sdk_marketplace_discovery.types.term_type


class LegalTerm(TypedDict, closed=True):
    id: "aws_sdk_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "aws_sdk_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    documents: "aws_sdk_marketplace_discovery.types.document_list.DocumentList"
    """<p>The legal documents proposed to the buyer as part of this term.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LegalTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_marketplace_discovery.types.term_type

    out["type"] = aws_sdk_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    import aws_sdk_marketplace_discovery.types.document_list

    out["documents"] = aws_sdk_marketplace_discovery.types.document_list.serialize_json(
        value["documents"]
    )
    return out


def deserialize_json(data: dict) -> LegalTerm:
    out: LegalTerm = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("LegalTerm.id required")
    if "type" in data:
        import aws_sdk_marketplace_discovery.types.term_type

        out["type"] = aws_sdk_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("LegalTerm.type required")
    if "documents" in data:
        import aws_sdk_marketplace_discovery.types.document_list

        out["documents"] = (
            aws_sdk_marketplace_discovery.types.document_list.deserialize_json(
                data["documents"]
            )
        )
    else:
        raise DeserializationError("LegalTerm.documents required")
    return out
