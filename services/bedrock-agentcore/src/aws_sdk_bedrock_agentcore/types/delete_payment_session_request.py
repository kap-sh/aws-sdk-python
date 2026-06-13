"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeletePaymentSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.payment_manager_arn
    import aws_sdk_bedrock_agentcore.types.payment_session_id
    import aws_sdk_bedrock_agentcore.types.user_id

class DeletePaymentSessionRequest(TypedDict):
    user_id: NotRequired["aws_sdk_bedrock_agentcore.types.user_id.UserId"]
    """<p>The user ID making the delete request. Must match the session's userId.</p>"""
    payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    """<p>The payment manager ARN. Must match the session's paymentManagerArn.</p>"""
    payment_session_id: "aws_sdk_bedrock_agentcore.types.payment_session_id.PaymentSessionId"
    """<p>The payment session ID to delete.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeletePaymentSessionRequest) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentSessionId"] = value["payment_session_id"]
    return out


def deserialize_json(data: dict) -> DeletePaymentSessionRequest:
    out: DeletePaymentSessionRequest = {}  # type: ignore[typeddict-item]
    if "paymentManagerArn" in data:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        raise DeserializationError("DeletePaymentSessionRequest.payment_manager_arn required")
    if "paymentSessionId" in data:
        out["payment_session_id"] = data["paymentSessionId"]
    else:
        raise DeserializationError("DeletePaymentSessionRequest.payment_session_id required")
    return out