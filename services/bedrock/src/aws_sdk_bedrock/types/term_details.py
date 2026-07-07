"""Generated from Smithy shape ``com.amazonaws.bedrock#TermDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.legal_term
    import aws_sdk_bedrock.types.pricing_term
    import aws_sdk_bedrock.types.support_term
    import aws_sdk_bedrock.types.validity_term


class TermDetails(TypedDict, closed=True):
    usage_based_pricing_term: "aws_sdk_bedrock.types.pricing_term.PricingTerm"
    legal_term: "aws_sdk_bedrock.types.legal_term.LegalTerm"
    """<p>Describes the legal terms.</p>"""
    support_term: "aws_sdk_bedrock.types.support_term.SupportTerm"
    """<p>Describes the support terms.</p>"""
    validity_term: NotRequired["aws_sdk_bedrock.types.validity_term.ValidityTerm"]
    """<p>Describes the validity terms.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TermDetails) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.pricing_term

    out["usageBasedPricingTerm"] = aws_sdk_bedrock.types.pricing_term.serialize_json(
        value["usage_based_pricing_term"]
    )
    import aws_sdk_bedrock.types.legal_term

    out["legalTerm"] = aws_sdk_bedrock.types.legal_term.serialize_json(
        value["legal_term"]
    )
    import aws_sdk_bedrock.types.support_term

    out["supportTerm"] = aws_sdk_bedrock.types.support_term.serialize_json(
        value["support_term"]
    )
    if "validity_term" in value:
        import aws_sdk_bedrock.types.validity_term

        out["validityTerm"] = aws_sdk_bedrock.types.validity_term.serialize_json(
            value["validity_term"]
        )
    return out


def deserialize_json(data: dict) -> TermDetails:
    out: TermDetails = {}  # type: ignore[typeddict-item]
    if "usageBasedPricingTerm" in data:
        import aws_sdk_bedrock.types.pricing_term

        out["usage_based_pricing_term"] = (
            aws_sdk_bedrock.types.pricing_term.deserialize_json(
                data["usageBasedPricingTerm"]
            )
        )
    else:
        raise DeserializationError("TermDetails.usage_based_pricing_term required")
    if "legalTerm" in data:
        import aws_sdk_bedrock.types.legal_term

        out["legal_term"] = aws_sdk_bedrock.types.legal_term.deserialize_json(
            data["legalTerm"]
        )
    else:
        raise DeserializationError("TermDetails.legal_term required")
    if "supportTerm" in data:
        import aws_sdk_bedrock.types.support_term

        out["support_term"] = aws_sdk_bedrock.types.support_term.deserialize_json(
            data["supportTerm"]
        )
    else:
        raise DeserializationError("TermDetails.support_term required")
    if "validityTerm" in data:
        import aws_sdk_bedrock.types.validity_term

        out["validity_term"] = aws_sdk_bedrock.types.validity_term.deserialize_json(
            data["validityTerm"]
        )
    return out
