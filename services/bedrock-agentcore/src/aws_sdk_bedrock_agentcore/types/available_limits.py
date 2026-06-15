"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AvailableLimits``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.amount
    import aws_sdk_bedrock_agentcore.types.date_timestamp


class AvailableLimits(TypedDict):
    available_spend_amount: NotRequired["aws_sdk_bedrock_agentcore.types.amount.Amount"]
    """<p>The remaining available amount that can be spent.</p>"""
    updated_at: NotRequired[
        "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    ]
    """<p>The timestamp when the available limits were last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AvailableLimits) -> dict:
    out: dict = {}
    if "available_spend_amount" in value:
        import aws_sdk_bedrock_agentcore.types.amount

        out["availableSpendAmount"] = (
            aws_sdk_bedrock_agentcore.types.amount.serialize_json(
                value["available_spend_amount"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["updatedAt"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> AvailableLimits:
    out: AvailableLimits = {}  # type: ignore[typeddict-item]
    if "availableSpendAmount" in data:
        import aws_sdk_bedrock_agentcore.types.amount

        out["available_spend_amount"] = (
            aws_sdk_bedrock_agentcore.types.amount.deserialize_json(
                data["availableSpendAmount"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
