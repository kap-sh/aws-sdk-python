"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentManagerSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.payment_manager_summary

PaymentManagerSummaries: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.payment_manager_summary.PaymentManagerSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentManagerSummaries) -> list:
    import aws_sdk_bedrock_agentcore_control.types.payment_manager_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.payment_manager_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PaymentManagerSummaries:
    import aws_sdk_bedrock_agentcore_control.types.payment_manager_summary

    out: PaymentManagerSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.payment_manager_summary.deserialize_json(
                item
            )
        )
    return out
