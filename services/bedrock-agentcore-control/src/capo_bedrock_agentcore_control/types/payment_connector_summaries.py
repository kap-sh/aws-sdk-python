"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentConnectorSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.payment_connector_summary

PaymentConnectorSummaries: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.payment_connector_summary.PaymentConnectorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentConnectorSummaries) -> list:
    import capo_bedrock_agentcore_control.types.payment_connector_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.payment_connector_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PaymentConnectorSummaries:
    import capo_bedrock_agentcore_control.types.payment_connector_summary

    out: PaymentConnectorSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.payment_connector_summary.deserialize_json(
                item
            )
        )
    return out
