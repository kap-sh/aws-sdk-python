"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Amount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.currency


class Amount(TypedDict, closed=True):
    value: "str"
    """<p>The numeric value of the amount.</p>"""
    currency: "capo_bedrock_agentcore.types.currency.Currency"
    """<p>The currency code for the amount.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Amount) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    import capo_bedrock_agentcore.types.currency

    out["currency"] = capo_bedrock_agentcore.types.currency.serialize_json(
        value["currency"]
    )
    return out


def deserialize_json(data: dict) -> Amount:
    out: Amount = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Amount.value required")
    if "currency" in data:
        import capo_bedrock_agentcore.types.currency

        out["currency"] = capo_bedrock_agentcore.types.currency.deserialize_json(
            data["currency"]
        )
    else:
        raise DeserializationError("Amount.currency required")
    return out
