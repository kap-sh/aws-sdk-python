"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentSession``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.available_limits
    import aws_sdk_bedrock_agentcore.types.date_timestamp
    import aws_sdk_bedrock_agentcore.types.payment_manager_arn
    import aws_sdk_bedrock_agentcore.types.payment_session_id
    import aws_sdk_bedrock_agentcore.types.session_limits
    import aws_sdk_bedrock_agentcore.types.user_id


class PaymentSession(TypedDict):
    payment_session_id: (
        "aws_sdk_bedrock_agentcore.types.payment_session_id.PaymentSessionId"
    )
    """<p>The unique identifier of the payment session.</p>"""
    payment_manager_arn: (
        "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The ARN of the payment manager that owns this session.</p>"""
    limits: NotRequired["aws_sdk_bedrock_agentcore.types.session_limits.SessionLimits"]
    """<p>The spending limits for the payment session.</p>"""
    user_id: "aws_sdk_bedrock_agentcore.types.user_id.UserId"
    """<p>The user ID associated with this session.</p>"""
    expiry_time_in_minutes: "int"
    """<p>The session expiry time in minutes.</p>"""
    created_at: "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the session was created.</p>"""
    available_limits: NotRequired[
        "aws_sdk_bedrock_agentcore.types.available_limits.AvailableLimits"
    ]
    """<p>The current available spending limits.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the session was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaymentSession) -> dict:
    out: dict = {}
    out["paymentSessionId"] = value["payment_session_id"]
    out["paymentManagerArn"] = value["payment_manager_arn"]
    if "limits" in value:
        import aws_sdk_bedrock_agentcore.types.session_limits

        out["limits"] = aws_sdk_bedrock_agentcore.types.session_limits.serialize_json(
            value["limits"]
        )
    out["userId"] = value["user_id"]
    out["expiryTimeInMinutes"] = value["expiry_time_in_minutes"]
    import aws_sdk_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    if "available_limits" in value:
        import aws_sdk_bedrock_agentcore.types.available_limits

        out["availableLimits"] = (
            aws_sdk_bedrock_agentcore.types.available_limits.serialize_json(
                value["available_limits"]
            )
        )
    import aws_sdk_bedrock_agentcore.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> PaymentSession:
    out: PaymentSession = {}  # type: ignore[typeddict-item]
    if "paymentSessionId" in data:
        out["payment_session_id"] = data["paymentSessionId"]
    else:
        raise DeserializationError("PaymentSession.payment_session_id required")
    if "paymentManagerArn" in data:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        raise DeserializationError("PaymentSession.payment_manager_arn required")
    if "limits" in data:
        import aws_sdk_bedrock_agentcore.types.session_limits

        out["limits"] = aws_sdk_bedrock_agentcore.types.session_limits.deserialize_json(
            data["limits"]
        )
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("PaymentSession.user_id required")
    if "expiryTimeInMinutes" in data:
        out["expiry_time_in_minutes"] = data["expiryTimeInMinutes"]
    else:
        raise DeserializationError("PaymentSession.expiry_time_in_minutes required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("PaymentSession.created_at required")
    if "availableLimits" in data:
        import aws_sdk_bedrock_agentcore.types.available_limits

        out["available_limits"] = (
            aws_sdk_bedrock_agentcore.types.available_limits.deserialize_json(
                data["availableLimits"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("PaymentSession.updated_at required")
    return out
