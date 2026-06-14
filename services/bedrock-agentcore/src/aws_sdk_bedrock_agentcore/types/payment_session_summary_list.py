"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentSessionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.payment_session_summary

PaymentSessionSummaryList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.payment_session_summary.PaymentSessionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentSessionSummaryList) -> list:
    import aws_sdk_bedrock_agentcore.types.payment_session_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore.types.payment_session_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PaymentSessionSummaryList:
    import aws_sdk_bedrock_agentcore.types.payment_session_summary

    out: PaymentSessionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.payment_session_summary.deserialize_json(
                item
            )
        )
    return out
