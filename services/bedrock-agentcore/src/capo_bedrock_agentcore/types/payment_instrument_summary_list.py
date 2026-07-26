"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentInstrumentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_instrument_summary

PaymentInstrumentSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore.types.payment_instrument_summary.PaymentInstrumentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentInstrumentSummaryList) -> list:
    import capo_bedrock_agentcore.types.payment_instrument_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.payment_instrument_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PaymentInstrumentSummaryList:
    import capo_bedrock_agentcore.types.payment_instrument_summary

    out: PaymentInstrumentSummaryList = []
    for item in data:
        out.append(
            capo_bedrock_agentcore.types.payment_instrument_summary.deserialize_json(
                item
            )
        )
    return out
