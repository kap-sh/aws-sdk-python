"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetPaymentInstrumentBalanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.blockchain_chain_id
    import aws_sdk_bedrock_agentcore.types.instrument_balance_token
    import aws_sdk_bedrock_agentcore.types.payment_agent_name
    import aws_sdk_bedrock_agentcore.types.payment_connector_id
    import aws_sdk_bedrock_agentcore.types.payment_instrument_id
    import aws_sdk_bedrock_agentcore.types.payment_manager_arn
    import aws_sdk_bedrock_agentcore.types.user_id


class GetPaymentInstrumentBalanceRequest(TypedDict, closed=True):
    user_id: NotRequired["aws_sdk_bedrock_agentcore.types.user_id.UserId"]
    """<p>The user ID associated with this payment instrument.</p>"""
    agent_name: NotRequired[
        "aws_sdk_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
    ]
    """<p>The agent name associated with this request, used for observability.</p>"""
    payment_manager_arn: (
        "aws_sdk_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn"
    )
    """<p>The ARN of the payment manager that owns this payment instrument.</p>"""
    payment_connector_id: (
        "aws_sdk_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
    )
    """<p>The ID of the payment connector associated with this instrument.</p>"""
    payment_instrument_id: (
        "aws_sdk_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId"
    )
    """<p>The ID of the payment instrument to query balance for.</p>"""
    chain: "aws_sdk_bedrock_agentcore.types.blockchain_chain_id.BlockchainChainId"
    """<p>The specific blockchain chain to query balance on. Required because balances are chain-specific.</p>"""
    token: "aws_sdk_bedrock_agentcore.types.instrument_balance_token.InstrumentBalanceToken"
    """<p>The token to query balance for. Only tokens supported for X402 payments are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentInstrumentBalanceRequest) -> dict:
    out: dict = {}
    out["paymentManagerArn"] = value["payment_manager_arn"]
    out["paymentConnectorId"] = value["payment_connector_id"]
    out["paymentInstrumentId"] = value["payment_instrument_id"]
    import aws_sdk_bedrock_agentcore.types.blockchain_chain_id

    out["chain"] = aws_sdk_bedrock_agentcore.types.blockchain_chain_id.serialize_json(
        value["chain"]
    )
    import aws_sdk_bedrock_agentcore.types.instrument_balance_token

    out["token"] = (
        aws_sdk_bedrock_agentcore.types.instrument_balance_token.serialize_json(
            value["token"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetPaymentInstrumentBalanceRequest:
    out: GetPaymentInstrumentBalanceRequest = {}  # type: ignore[typeddict-item]
    if "paymentManagerArn" in data:
        out["payment_manager_arn"] = data["paymentManagerArn"]
    else:
        raise DeserializationError(
            "GetPaymentInstrumentBalanceRequest.payment_manager_arn required"
        )
    if "paymentConnectorId" in data:
        out["payment_connector_id"] = data["paymentConnectorId"]
    else:
        raise DeserializationError(
            "GetPaymentInstrumentBalanceRequest.payment_connector_id required"
        )
    if "paymentInstrumentId" in data:
        out["payment_instrument_id"] = data["paymentInstrumentId"]
    else:
        raise DeserializationError(
            "GetPaymentInstrumentBalanceRequest.payment_instrument_id required"
        )
    if "chain" in data:
        import aws_sdk_bedrock_agentcore.types.blockchain_chain_id

        out["chain"] = (
            aws_sdk_bedrock_agentcore.types.blockchain_chain_id.deserialize_json(
                data["chain"]
            )
        )
    else:
        raise DeserializationError("GetPaymentInstrumentBalanceRequest.chain required")
    if "token" in data:
        import aws_sdk_bedrock_agentcore.types.instrument_balance_token

        out["token"] = (
            aws_sdk_bedrock_agentcore.types.instrument_balance_token.deserialize_json(
                data["token"]
            )
        )
    else:
        raise DeserializationError("GetPaymentInstrumentBalanceRequest.token required")
    return out
