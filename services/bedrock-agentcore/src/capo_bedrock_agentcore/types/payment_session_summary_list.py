"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentSessionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_session_summary

PaymentSessionSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore.types.payment_session_summary.PaymentSessionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentSessionSummaryList) -> list:
    import capo_bedrock_agentcore.types.payment_session_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore.types.payment_session_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PaymentSessionSummaryList:
    import capo_bedrock_agentcore.types.payment_session_summary

    out: PaymentSessionSummaryList = []
    for item in data:
        out.append(
            capo_bedrock_agentcore.types.payment_session_summary.deserialize_json(item)
        )
    return out
