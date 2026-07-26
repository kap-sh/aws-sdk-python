"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#FreeTrialPricingTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.bounded_string
    import capo_marketplace_discovery.types.grant_list
    import capo_marketplace_discovery.types.term_id
    import capo_marketplace_discovery.types.term_type


class FreeTrialPricingTerm(TypedDict, closed=True):
    id: "capo_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "capo_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    duration: NotRequired[
        "capo_marketplace_discovery.types.bounded_string.BoundedString"
    ]
    """<p>The duration of the free trial period.</p>"""
    grants: "capo_marketplace_discovery.types.grant_list.GrantList"
    """<p>The entitlements granted to the buyer during the free trial.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialPricingTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_marketplace_discovery.types.term_type

    out["type"] = capo_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    if "duration" in value:
        out["duration"] = value["duration"]
    import capo_marketplace_discovery.types.grant_list

    out["grants"] = capo_marketplace_discovery.types.grant_list.serialize_json(
        value["grants"]
    )
    return out


def deserialize_json(data: dict) -> FreeTrialPricingTerm:
    out: FreeTrialPricingTerm = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FreeTrialPricingTerm.id required")
    if "type" in data:
        import capo_marketplace_discovery.types.term_type

        out["type"] = capo_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("FreeTrialPricingTerm.type required")
    if "duration" in data:
        out["duration"] = data["duration"]
    if "grants" in data:
        import capo_marketplace_discovery.types.grant_list

        out["grants"] = capo_marketplace_discovery.types.grant_list.deserialize_json(
            data["grants"]
        )
    else:
        raise DeserializationError("FreeTrialPricingTerm.grants required")
    return out
