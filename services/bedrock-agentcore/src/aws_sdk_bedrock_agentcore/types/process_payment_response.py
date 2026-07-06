"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ProcessPaymentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.date_timestamp
    import aws_sdk_bedrock_agentcore.types.payment_instrument_id
    import aws_sdk_bedrock_agentcore.types.payment_manager_arn
    import aws_sdk_bedrock_agentcore.types.payment_output
    import aws_sdk_bedrock_agentcore.types.payment_session_id
    import aws_sdk_bedrock_agentcore.types.payment_status
    import aws_sdk_bedrock_agentcore.types.payment_type
    import aws_sdk_bedrock_agentcore.types.process_payment_id


class ProcessPaymentResponse(TypedDict, closed=True):
    process_payment_id: (
        "aws_sdk_bedrock_agentcore.types.process_payment_id.ProcessPaymentId"
    )
    """<p>The unique identifier of the processed payment.</p>"""
    payment_manager_arn: (
        "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The ARN of the payment manager.</p>"""
    payment_session_id: (
        "aws_sdk_bedrock_agentcore.types.payment_session_id.PaymentSessionId"
    )
    """<p>The ID of the payment session used.</p>"""
    payment_instrument_id: (
        "aws_sdk_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId"
    )
    """<p>The ID of the payment instrument used.</p>"""
    payment_type: "aws_sdk_bedrock_agentcore.types.payment_type.PaymentType"
    """<p>The type of payment processed.</p>"""
    status: "aws_sdk_bedrock_agentcore.types.payment_status.PaymentStatus"
    """<p>The status of the payment.</p>"""
    payment_output: "aws_sdk_bedrock_agentcore.types.payment_output.PaymentOutput"
    """<p>The payment output details specific to the payment type.</p>"""
    created_at: "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment was created.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProcessPaymentResponse) -> dict:
    out: dict = {}
    out["processPaymentId"] = value["process_payment_id"]
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentSessionId"] = value["payment_session_id"]
    out["paymentInstrumentId"] = value["payment_instrument_id"]
    import aws_sdk_bedrock_agentcore.types.payment_type

    out["paymentType"] = aws_sdk_bedrock_agentcore.types.payment_type.serialize_json(
        value["payment_type"]
    )
    import aws_sdk_bedrock_agentcore.types.payment_status

    out["status"] = aws_sdk_bedrock_agentcore.types.payment_status.serialize_json(
        value["status"]
    )
    import aws_sdk_bedrock_agentcore.types.payment_output

    out["paymentOutput"] = (
        aws_sdk_bedrock_agentcore.types.payment_output.serialize_json(
            value["payment_output"]
        )
    )
    import aws_sdk_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock_agentcore.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> ProcessPaymentResponse:
    out: ProcessPaymentResponse = {}  # type: ignore[typeddict-item]
    if "processPaymentId" in data:
        out["process_payment_id"] = data["processPaymentId"]
    else:
        raise DeserializationError("ProcessPaymentResponse.process_payment_id required")
    if "paymentManagerArn" in data:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        raise DeserializationError(
            "ProcessPaymentResponse.payment_manager_arn required"
        )
    if "paymentSessionId" in data:
        out["payment_session_id"] = data["paymentSessionId"]
    else:
        raise DeserializationError("ProcessPaymentResponse.payment_session_id required")
    if "paymentInstrumentId" in data:
        out["payment_instrument_id"] = data["paymentInstrumentId"]
    else:
        raise DeserializationError(
            "ProcessPaymentResponse.payment_instrument_id required"
        )
    if "paymentType" in data:
        import aws_sdk_bedrock_agentcore.types.payment_type

        out["payment_type"] = (
            aws_sdk_bedrock_agentcore.types.payment_type.deserialize_json(
                data["paymentType"]
            )
        )
    else:
        raise DeserializationError("ProcessPaymentResponse.payment_type required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.payment_status

        out["status"] = aws_sdk_bedrock_agentcore.types.payment_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ProcessPaymentResponse.status required")
    if "paymentOutput" in data:
        import aws_sdk_bedrock_agentcore.types.payment_output

        out["payment_output"] = (
            aws_sdk_bedrock_agentcore.types.payment_output.deserialize_json(
                data["paymentOutput"]
            )
        )
    else:
        raise DeserializationError("ProcessPaymentResponse.payment_output required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("ProcessPaymentResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("ProcessPaymentResponse.updated_at required")
    return out
