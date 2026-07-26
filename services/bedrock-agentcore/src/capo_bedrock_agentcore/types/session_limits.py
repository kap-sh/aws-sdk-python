"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SessionLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.amount


class SessionLimits(TypedDict, closed=True):
    max_spend_amount: "capo_bedrock_agentcore.types.amount.Amount"
    """<p>The maximum amount that can be spent in the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionLimits) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.amount

    out["maxSpendAmount"] = capo_bedrock_agentcore.types.amount.serialize_json(
        value["max_spend_amount"]
    )
    return out


def deserialize_json(data: dict) -> SessionLimits:
    out: SessionLimits = {}  # type: ignore[typeddict-item]
    if "maxSpendAmount" in data:
        import capo_bedrock_agentcore.types.amount

        out["max_spend_amount"] = capo_bedrock_agentcore.types.amount.deserialize_json(
            data["maxSpendAmount"]
        )
    else:
        raise DeserializationError("SessionLimits.max_spend_amount required")
    return out
