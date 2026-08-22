"""Generated from Smithy shape ``com.amazonaws.bedrock#TermDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.legal_term
    import capo_bedrock.types.pricing_term
    import capo_bedrock.types.support_term
    import capo_bedrock.types.validity_term


class TermDetails(TypedDict, closed=True):
    usage_based_pricing_term: "capo_bedrock.types.pricing_term.PricingTerm"
    legal_term: "capo_bedrock.types.legal_term.LegalTerm"
    """<p>Describes the legal terms.</p>"""
    support_term: "capo_bedrock.types.support_term.SupportTerm"
    """<p>Describes the support terms.</p>"""
    validity_term: NotRequired["capo_bedrock.types.validity_term.ValidityTerm"]
    """<p>Describes the validity terms.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TermDetails) -> dict:
    out: dict = {}
    import capo_bedrock.types.pricing_term

    out["usageBasedPricingTerm"] = capo_bedrock.types.pricing_term.serialize_json(
        value["usage_based_pricing_term"]
    )
    import capo_bedrock.types.legal_term

    out["legalTerm"] = capo_bedrock.types.legal_term.serialize_json(value["legal_term"])
    import capo_bedrock.types.support_term

    out["supportTerm"] = capo_bedrock.types.support_term.serialize_json(
        value["support_term"]
    )
    if "validity_term" in value:
        import capo_bedrock.types.validity_term

        out["validityTerm"] = capo_bedrock.types.validity_term.serialize_json(
            value["validity_term"]
        )
    return out


def deserialize_json(data: dict) -> TermDetails:
    out: TermDetails = {}  # type: ignore[typeddict-item]
    if data.get("usageBasedPricingTerm") is not None:
        import capo_bedrock.types.pricing_term

        out["usage_based_pricing_term"] = (
            capo_bedrock.types.pricing_term.deserialize_json(
                data["usageBasedPricingTerm"]
            )
        )
    else:
        raise DeserializationError("TermDetails.usage_based_pricing_term required")
    if data.get("legalTerm") is not None:
        import capo_bedrock.types.legal_term

        out["legal_term"] = capo_bedrock.types.legal_term.deserialize_json(
            data["legalTerm"]
        )
    else:
        raise DeserializationError("TermDetails.legal_term required")
    if data.get("supportTerm") is not None:
        import capo_bedrock.types.support_term

        out["support_term"] = capo_bedrock.types.support_term.deserialize_json(
            data["supportTerm"]
        )
    else:
        raise DeserializationError("TermDetails.support_term required")
    if data.get("validityTerm") is not None:
        import capo_bedrock.types.validity_term

        out["validity_term"] = capo_bedrock.types.validity_term.deserialize_json(
            data["validityTerm"]
        )
    return out
