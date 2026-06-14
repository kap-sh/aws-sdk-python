"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetPaymentSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.payment_agent_name
    import aws_sdk_bedrock_agentcore.types.payment_manager_arn
    import aws_sdk_bedrock_agentcore.types.payment_session_id
    import aws_sdk_bedrock_agentcore.types.user_id


class GetPaymentSessionRequest(TypedDict):
    user_id: NotRequired["aws_sdk_bedrock_agentcore.types.user_id.UserId"]
    """<p>The user ID associated with this payment session.</p>"""
    agent_name: NotRequired[
        "aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
    ]
    """<p>The agent name associated with this request, used for observability.</p>"""
    payment_manager_arn: (
        "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The ARN of the payment manager that owns this session.</p>"""
    payment_session_id: (
        "aws_sdk_bedrock_agentcore.types.payment_session_id.PaymentSessionId"
    )
    """<p>The ID of the payment session to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentSessionRequest) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentSessionId"] = value["payment_session_id"]
    return out


def deserialize_json(data: dict) -> GetPaymentSessionRequest:
    out: GetPaymentSessionRequest = {}  # type: ignore[typeddict-item]
    if "paymentManagerArn" in data:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        raise DeserializationError(
            "GetPaymentSessionRequest.payment_manager_arn required"
        )
    if "paymentSessionId" in data:
        out["payment_session_id"] = data["paymentSessionId"]
    else:
        raise DeserializationError(
            "GetPaymentSessionRequest.payment_session_id required"
        )
    return out
