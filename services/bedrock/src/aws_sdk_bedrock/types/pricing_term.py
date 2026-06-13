"""Generated from Smithy shape ``com.amazonaws.bedrock#PricingTerm``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.rate_card


class PricingTerm(TypedDict):
    rate_card: "aws_sdk_bedrock.types.rate_card.RateCard"
    """<p>Describes a usage price for each dimension.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PricingTerm) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.rate_card

    out["rateCard"] = aws_sdk_bedrock.types.rate_card.serialize_json(value["rate_card"])
    return out


def deserialize_json(data: dict) -> PricingTerm:
    out: PricingTerm = {}  # type: ignore[typeddict-item]
    if "rateCard" in data:
        import aws_sdk_bedrock.types.rate_card

        out["rate_card"] = aws_sdk_bedrock.types.rate_card.deserialize_json(
            data["rateCard"]
        )
    else:
        raise DeserializationError("PricingTerm.rate_card required")
    return out
