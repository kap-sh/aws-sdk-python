"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentInstrument``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.date_timestamp
    import aws_sdk_bedrock_agentcore.types.payment_connector_id
    import aws_sdk_bedrock_agentcore.types.payment_instrument_details
    import aws_sdk_bedrock_agentcore.types.payment_instrument_id
    import aws_sdk_bedrock_agentcore.types.payment_instrument_status
    import aws_sdk_bedrock_agentcore.types.payment_instrument_type
    import aws_sdk_bedrock_agentcore.types.payment_manager_arn
    import aws_sdk_bedrock_agentcore.types.user_id


class PaymentInstrument(TypedDict):
    payment_instrument_id: (
        "aws_sdk_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId"
    )
    """<p>The unique identifier for this payment instrument.</p>"""
    payment_manager_arn: (
        "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The ARN of the payment manager that owns this payment instrument.</p>"""
    payment_connector_id: (
        "aws_sdk_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
    )
    """<p>The ID of the payment connector associated with this instrument.</p>"""
    user_id: "aws_sdk_bedrock_agentcore.types.user_id.UserId"
    """<p>The user ID associated with this payment instrument.</p>"""
    payment_instrument_type: (
        "aws_sdk_bedrock_agentcore.types.payment_instrument_type.PaymentInstrumentType"
    )
    """<p>The type of payment instrument (e.g., EMBEDDED_CRYPTO_WALLET).</p>"""
    payment_instrument_details: "aws_sdk_bedrock_agentcore.types.payment_instrument_details.PaymentInstrumentDetails"
    """<p>The details specific to the payment instrument type.</p>"""
    created_at: "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when this payment instrument was created.</p>"""
    status: "aws_sdk_bedrock_agentcore.types.payment_instrument_status.PaymentInstrumentStatus"
    """<p>The current status of this payment instrument.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when this payment instrument was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaymentInstrument) -> dict:
    out: dict = {}
    out["paymentInstrumentId"] = value["payment_instrument_id"]
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentConnectorId"] = value["payment_connector_id"]
    out["userId"] = value["user_id"]
    import aws_sdk_bedrock_agentcore.types.payment_instrument_type

    out["paymentInstrumentType"] = (
        aws_sdk_bedrock_agentcore.types.payment_instrument_type.serialize_json(
            value["payment_instrument_type"]
        )
    )
    import aws_sdk_bedrock_agentcore.types.payment_instrument_details

    out["paymentInstrumentDetails"] = (
        aws_sdk_bedrock_agentcore.types.payment_instrument_details.serialize_json(
            value["payment_instrument_details"]
        )
    )
    import aws_sdk_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock_agentcore.types.payment_instrument_status

    out["status"] = (
        aws_sdk_bedrock_agentcore.types.payment_instrument_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_bedrock_agentcore.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> PaymentInstrument:
    out: PaymentInstrument = {}  # type: ignore[typeddict-item]
    if "paymentInstrumentId" in data:
        out["payment_instrument_id"] = data["paymentInstrumentId"]
    else:
        raise DeserializationError("PaymentInstrument.payment_instrument_id required")
    if "paymentManagerArn" in data:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        raise DeserializationError("PaymentInstrument.payment_manager_arn required")
    if "paymentConnectorId" in data:
        out["payment_connector_id"] = data["paymentConnectorId"]
    else:
        raise DeserializationError("PaymentInstrument.payment_connector_id required")
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("PaymentInstrument.user_id required")
    if "paymentInstrumentType" in data:
        import aws_sdk_bedrock_agentcore.types.payment_instrument_type

        out["payment_instrument_type"] = (
            aws_sdk_bedrock_agentcore.types.payment_instrument_type.deserialize_json(
                data["paymentInstrumentType"]
            )
        )
    else:
        raise DeserializationError("PaymentInstrument.payment_instrument_type required")
    if "paymentInstrumentDetails" in data:
        import aws_sdk_bedrock_agentcore.types.payment_instrument_details

        out["payment_instrument_details"] = (
            aws_sdk_bedrock_agentcore.types.payment_instrument_details.deserialize_json(
                data["paymentInstrumentDetails"]
            )
        )
    else:
        raise DeserializationError(
            "PaymentInstrument.payment_instrument_details required"
        )
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("PaymentInstrument.created_at required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.payment_instrument_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.payment_instrument_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("PaymentInstrument.status required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("PaymentInstrument.updated_at required")
    return out
