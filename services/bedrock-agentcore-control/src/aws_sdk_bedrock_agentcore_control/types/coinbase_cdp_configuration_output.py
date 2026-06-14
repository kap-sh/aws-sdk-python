"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CoinbaseCdpConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.coinbase_cdp_api_key_id_type
    import aws_sdk_bedrock_agentcore_control.types.secret
    import aws_sdk_bedrock_agentcore_control.types.secret_json_key_type
    import aws_sdk_bedrock_agentcore_control.types.secret_source_type


class CoinbaseCdpConfigurationOutput(TypedDict):
    api_key_id: "aws_sdk_bedrock_agentcore_control.types.coinbase_cdp_api_key_id_type.CoinbaseCdpApiKeyIdType"
    """<p>The API key identifier provided by Coinbase Developer Platform.</p>"""
    api_key_secret_arn: "aws_sdk_bedrock_agentcore_control.types.secret.Secret"
    api_key_secret_json_key: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_json_key_type.SecretJsonKeyType"
    ]
    """<p>The JSON key used to extract the API key secret value from the AWS Secrets Manager secret.</p>"""
    api_key_secret_source: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the API key secret. Either <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if managed by the user in AWS Secrets Manager.</p>"""
    wallet_secret_arn: "aws_sdk_bedrock_agentcore_control.types.secret.Secret"
    wallet_secret_json_key: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_json_key_type.SecretJsonKeyType"
    ]
    """<p>The JSON key used to extract the wallet secret value from the AWS Secrets Manager secret.</p>"""
    wallet_secret_source: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the wallet secret. Either <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if managed by the user in AWS Secrets Manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoinbaseCdpConfigurationOutput) -> dict:
    out: dict = {}
    out["apiKeyId"] = value["api_key_id"]
    import aws_sdk_bedrock_agentcore_control.types.secret

    out["apiKeySecretArn"] = (
        aws_sdk_bedrock_agentcore_control.types.secret.serialize_json(
            value["api_key_secret_arn"]
        )
    )
    if "api_key_secret_json_key" in value:
        out["apiKeySecretJsonKey"] = value["api_key_secret_json_key"]
    if "api_key_secret_source" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["apiKeySecretSource"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["api_key_secret_source"]
            )
        )
    import aws_sdk_bedrock_agentcore_control.types.secret

    out["walletSecretArn"] = (
        aws_sdk_bedrock_agentcore_control.types.secret.serialize_json(
            value["wallet_secret_arn"]
        )
    )
    if "wallet_secret_json_key" in value:
        out["walletSecretJsonKey"] = value["wallet_secret_json_key"]
    if "wallet_secret_source" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["walletSecretSource"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["wallet_secret_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoinbaseCdpConfigurationOutput:
    out: CoinbaseCdpConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "apiKeyId" in data:
        out["api_key_id"] = data["apiKeyId"]
    else:
        raise DeserializationError("CoinbaseCdpConfigurationOutput.api_key_id required")
    if "apiKeySecretArn" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret

        out["api_key_secret_arn"] = (
            aws_sdk_bedrock_agentcore_control.types.secret.deserialize_json(
                data["apiKeySecretArn"]
            )
        )
    else:
        raise DeserializationError(
            "CoinbaseCdpConfigurationOutput.api_key_secret_arn required"
        )
    if "apiKeySecretJsonKey" in data:
        out["api_key_secret_json_key"] = data["apiKeySecretJsonKey"]
    if "apiKeySecretSource" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["api_key_secret_source"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["apiKeySecretSource"]
            )
        )
    if "walletSecretArn" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret

        out["wallet_secret_arn"] = (
            aws_sdk_bedrock_agentcore_control.types.secret.deserialize_json(
                data["walletSecretArn"]
            )
        )
    else:
        raise DeserializationError(
            "CoinbaseCdpConfigurationOutput.wallet_secret_arn required"
        )
    if "walletSecretJsonKey" in data:
        out["wallet_secret_json_key"] = data["walletSecretJsonKey"]
    if "walletSecretSource" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["wallet_secret_source"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["walletSecretSource"]
            )
        )
    return out
