"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetPaymentInstrumentRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.payment_agent_name
    import aws_sdk_bedrock_agentcore.types.payment_connector_id
    import aws_sdk_bedrock_agentcore.types.payment_instrument_id
    import aws_sdk_bedrock_agentcore.types.payment_manager_arn
    import aws_sdk_bedrock_agentcore.types.user_id

class GetPaymentInstrumentRequest(TypedDict):
    user_id: NotRequired["aws_sdk_bedrock_agentcore.types.user_id.UserId"]
    """<p>The user ID associated with this payment instrument.</p>"""
    agent_name: NotRequired["aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"]
    """<p>The agent name associated with this request, used for observability.</p>"""
    payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    """<p>The ARN of the payment manager that owns this payment instrument.</p>"""
    payment_connector_id: NotRequired["aws_sdk_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"]
    """<p>The ID of the payment connector.</p>"""
    payment_instrument_id: "aws_sdk_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId"
    """<p>The ID of the payment instrument to retrieve.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentInstrumentRequest) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    if "payment_connector_id" in value:
        out["paymentConnectorId"] = value["payment_connector_id"]
    out["paymentInstrumentId"] = value["payment_instrument_id"]
    return out


def deserialize_json(data: dict) -> GetPaymentInstrumentRequest:
    out: GetPaymentInstrumentRequest = {}  # type: ignore[typeddict-item]
    if "paymentManagerArn" in data:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        raise DeserializationError("GetPaymentInstrumentRequest.payment_manager_arn required")
    if "paymentConnectorId" in data:
        out["payment_connector_id"] = data["paymentConnectorId"]
    if "paymentInstrumentId" in data:
        out["payment_instrument_id"] = data["paymentInstrumentId"]
    else:
        raise DeserializationError("GetPaymentInstrumentRequest.payment_instrument_id required")
    return out