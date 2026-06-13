"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeletePaymentInstrumentRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.payment_connector_id
    import aws_sdk_bedrock_agentcore.types.payment_instrument_id
    import aws_sdk_bedrock_agentcore.types.payment_manager_arn
    import aws_sdk_bedrock_agentcore.types.user_id

class DeletePaymentInstrumentRequest(TypedDict):
    user_id: NotRequired["aws_sdk_bedrock_agentcore.types.user_id.UserId"]
    """<p>The user ID making the delete request. Must match the instrument's userId.</p>"""
    payment_manager_arn: "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    """<p>The payment manager ARN. Must match the instrument's paymentManagerArn.</p>"""
    payment_connector_id: "aws_sdk_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
    """<p>The payment connector ID. Must match the instrument's paymentConnectorId.</p>"""
    payment_instrument_id: "aws_sdk_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId"
    """<p>The payment instrument ID to delete.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeletePaymentInstrumentRequest) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentConnectorId"] = value["payment_connector_id"]
    out["paymentInstrumentId"] = value["payment_instrument_id"]
    return out


def deserialize_json(data: dict) -> DeletePaymentInstrumentRequest:
    out: DeletePaymentInstrumentRequest = {}  # type: ignore[typeddict-item]
    if "paymentManagerArn" in data:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        raise DeserializationError("DeletePaymentInstrumentRequest.payment_manager_arn required")
    if "paymentConnectorId" in data:
        out["payment_connector_id"] = data["paymentConnectorId"]
    else:
        raise DeserializationError("DeletePaymentInstrumentRequest.payment_connector_id required")
    if "paymentInstrumentId" in data:
        out["payment_instrument_id"] = data["paymentInstrumentId"]
    else:
        raise DeserializationError("DeletePaymentInstrumentRequest.payment_instrument_id required")
    return out