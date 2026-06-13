"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SupportTerm``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.bounded_string
    import aws_sdk_marketplace_discovery.types.term_id
    import aws_sdk_marketplace_discovery.types.term_type


class SupportTerm(TypedDict):
    id: "aws_sdk_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "aws_sdk_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    refund_policy: "aws_sdk_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The refund policy description for the offer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SupportTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_marketplace_discovery.types.term_type

    out["type"] = aws_sdk_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    out["refundPolicy"] = value["refund_policy"]
    return out


def deserialize_json(data: dict) -> SupportTerm:
    out: SupportTerm = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("SupportTerm.id required")
    if "type" in data:
        import aws_sdk_marketplace_discovery.types.term_type

        out["type"] = aws_sdk_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("SupportTerm.type required")
    if "refundPolicy" in data:
        out["refund_policy"] = data["refundPolicy"]
    else:
        raise DeserializationError("SupportTerm.refund_policy required")
    return out
