"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#RenewalTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.term_id
    import capo_marketplace_discovery.types.term_type


class RenewalTerm(TypedDict, closed=True):
    id: "capo_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "capo_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RenewalTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_marketplace_discovery.types.term_type

    out["type"] = capo_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> RenewalTerm:
    out: RenewalTerm = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("RenewalTerm.id required")
    if "type" in data:
        import capo_marketplace_discovery.types.term_type

        out["type"] = capo_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("RenewalTerm.type required")
    return out
