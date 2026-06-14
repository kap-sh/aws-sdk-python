"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StripePrivyConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.secret
    import aws_sdk_bedrock_agentcore_control.types.secret_json_key_type
    import aws_sdk_bedrock_agentcore_control.types.secret_source_type
    import aws_sdk_bedrock_agentcore_control.types.stripe_privy_app_id_type
    import aws_sdk_bedrock_agentcore_control.types.stripe_privy_authorization_id_type


class StripePrivyConfigurationOutput(TypedDict):
    app_id: "aws_sdk_bedrock_agentcore_control.types.stripe_privy_app_id_type.StripePrivyAppIdType"
    """<p>The app ID provided by Privy.</p>"""
    app_secret_arn: "aws_sdk_bedrock_agentcore_control.types.secret.Secret"
    app_secret_json_key: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_json_key_type.SecretJsonKeyType"
    ]
    """<p>The JSON key used to extract the app secret value from the AWS Secrets Manager secret.</p>"""
    app_secret_source: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the app secret. Either <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if managed by the user in AWS Secrets Manager.</p>"""
    authorization_private_key_arn: (
        "aws_sdk_bedrock_agentcore_control.types.secret.Secret"
    )
    authorization_private_key_json_key: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_json_key_type.SecretJsonKeyType"
    ]
    """<p>The JSON key used to extract the authorization private key value from the AWS Secrets Manager secret.</p>"""
    authorization_private_key_source: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the authorization private key. Either <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if managed by the user in AWS Secrets Manager.</p>"""
    authorization_id: "aws_sdk_bedrock_agentcore_control.types.stripe_privy_authorization_id_type.StripePrivyAuthorizationIdType"
    """<p>The authorization ID for the Stripe Privy integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StripePrivyConfigurationOutput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    import aws_sdk_bedrock_agentcore_control.types.secret

    out["appSecretArn"] = aws_sdk_bedrock_agentcore_control.types.secret.serialize_json(
        value["app_secret_arn"]
    )
    if "app_secret_json_key" in value:
        out["appSecretJsonKey"] = value["app_secret_json_key"]
    if "app_secret_source" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["appSecretSource"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["app_secret_source"]
            )
        )
    import aws_sdk_bedrock_agentcore_control.types.secret

    out["authorizationPrivateKeyArn"] = (
        aws_sdk_bedrock_agentcore_control.types.secret.serialize_json(
            value["authorization_private_key_arn"]
        )
    )
    if "authorization_private_key_json_key" in value:
        out["authorizationPrivateKeyJsonKey"] = value[
            "authorization_private_key_json_key"
        ]
    if "authorization_private_key_source" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["authorizationPrivateKeySource"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["authorization_private_key_source"]
            )
        )
    out["authorizationId"] = value["authorization_id"]
    return out


def deserialize_json(data: dict) -> StripePrivyConfigurationOutput:
    out: StripePrivyConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("StripePrivyConfigurationOutput.app_id required")
    if "appSecretArn" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret

        out["app_secret_arn"] = (
            aws_sdk_bedrock_agentcore_control.types.secret.deserialize_json(
                data["appSecretArn"]
            )
        )
    else:
        raise DeserializationError(
            "StripePrivyConfigurationOutput.app_secret_arn required"
        )
    if "appSecretJsonKey" in data:
        out["app_secret_json_key"] = data["appSecretJsonKey"]
    if "appSecretSource" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["app_secret_source"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["appSecretSource"]
            )
        )
    if "authorizationPrivateKeyArn" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret

        out["authorization_private_key_arn"] = (
            aws_sdk_bedrock_agentcore_control.types.secret.deserialize_json(
                data["authorizationPrivateKeyArn"]
            )
        )
    else:
        raise DeserializationError(
            "StripePrivyConfigurationOutput.authorization_private_key_arn required"
        )
    if "authorizationPrivateKeyJsonKey" in data:
        out["authorization_private_key_json_key"] = data[
            "authorizationPrivateKeyJsonKey"
        ]
    if "authorizationPrivateKeySource" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["authorization_private_key_source"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["authorizationPrivateKeySource"]
            )
        )
    if "authorizationId" in data:
        out["authorization_id"] = data["authorizationId"]
    else:
        raise DeserializationError(
            "StripePrivyConfigurationOutput.authorization_id required"
        )
    return out
