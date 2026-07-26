"""Generated from Smithy shape ``com.amazonaws.sesv2#EmailAddressInsightsVerdict``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_address_insights_confidence_verdict


class EmailAddressInsightsVerdict(TypedDict, closed=True):
    confidence_verdict: NotRequired[
        "capo_sesv2.types.email_address_insights_confidence_verdict.EmailAddressInsightsConfidenceVerdict"
    ]
    """<p>The confidence level of the validation verdict.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressInsightsVerdict) -> dict:
    out: dict = {}
    if "confidence_verdict" in value:
        import capo_sesv2.types.email_address_insights_confidence_verdict

        out["ConfidenceVerdict"] = (
            capo_sesv2.types.email_address_insights_confidence_verdict.serialize_json(
                value["confidence_verdict"]
            )
        )
    return out


def deserialize_json(data: dict) -> EmailAddressInsightsVerdict:
    out: EmailAddressInsightsVerdict = {}  # type: ignore[typeddict-item]
    if "ConfidenceVerdict" in data:
        import capo_sesv2.types.email_address_insights_confidence_verdict

        out["confidence_verdict"] = (
            capo_sesv2.types.email_address_insights_confidence_verdict.deserialize_json(
                data["ConfidenceVerdict"]
            )
        )
    return out
