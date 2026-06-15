"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ProcessPaymentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.client_token
    import aws_sdk_bedrock_agentcore.types.payment_agent_name
    import aws_sdk_bedrock_agentcore.types.payment_input
    import aws_sdk_bedrock_agentcore.types.payment_instrument_id
    import aws_sdk_bedrock_agentcore.types.payment_manager_arn
    import aws_sdk_bedrock_agentcore.types.payment_session_id
    import aws_sdk_bedrock_agentcore.types.payment_type
    import aws_sdk_bedrock_agentcore.types.user_id


class ProcessPaymentRequest(TypedDict):
    user_id: NotRequired["aws_sdk_bedrock_agentcore.types.user_id.UserId"]
    """<p>The user ID associated with this payment.</p>"""
    agent_name: NotRequired[
        "aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
    ]
    """<p>The agent name associated with this request, used for observability.</p>"""
    payment_manager_arn: (
        "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The ARN of the payment manager.</p>"""
    payment_session_id: (
        "aws_sdk_bedrock_agentcore.types.payment_session_id.PaymentSessionId"
    )
    """<p>The ID of the payment session.</p>"""
    payment_instrument_id: (
        "aws_sdk_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId"
    )
    """<p>The ID of the payment instrument to use.</p>"""
    payment_type: "aws_sdk_bedrock_agentcore.types.payment_type.PaymentType"
    """<p>The type of payment to process.</p>"""
    payment_input: "aws_sdk_bedrock_agentcore.types.payment_input.PaymentInput"
    """<p>The payment input details specific to the payment type.</p>"""
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProcessPaymentRequest) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentSessionId"] = value["payment_session_id"]
    out["paymentInstrumentId"] = value["payment_instrument_id"]
    import aws_sdk_bedrock_agentcore.types.payment_type

    out["paymentType"] = aws_sdk_bedrock_agentcore.types.payment_type.serialize_json(
        value["payment_type"]
    )
    import aws_sdk_bedrock_agentcore.types.payment_input

    out["paymentInput"] = aws_sdk_bedrock_agentcore.types.payment_input.serialize_json(
        value["payment_input"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ProcessPaymentRequest:
    out: ProcessPaymentRequest = {}  # type: ignore[typeddict-item]
    if "paymentManagerArn" in data:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        raise DeserializationError("ProcessPaymentRequest.payment_manager_arn required")
    if "paymentSessionId" in data:
        out["payment_session_id"] = data["paymentSessionId"]
    else:
        raise DeserializationError("ProcessPaymentRequest.payment_session_id required")
    if "paymentInstrumentId" in data:
        out["payment_instrument_id"] = data["paymentInstrumentId"]
    else:
        raise DeserializationError(
            "ProcessPaymentRequest.payment_instrument_id required"
        )
    if "paymentType" in data:
        import aws_sdk_bedrock_agentcore.types.payment_type

        out["payment_type"] = (
            aws_sdk_bedrock_agentcore.types.payment_type.deserialize_json(
                data["paymentType"]
            )
        )
    else:
        raise DeserializationError("ProcessPaymentRequest.payment_type required")
    if "paymentInput" in data:
        import aws_sdk_bedrock_agentcore.types.payment_input

        out["payment_input"] = (
            aws_sdk_bedrock_agentcore.types.payment_input.deserialize_json(
                data["paymentInput"]
            )
        )
    else:
        raise DeserializationError("ProcessPaymentRequest.payment_input required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
