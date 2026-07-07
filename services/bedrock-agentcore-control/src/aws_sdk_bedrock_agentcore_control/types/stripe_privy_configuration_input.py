"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StripePrivyConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.default_stripe_privy_app_secret_type
    import aws_sdk_bedrock_agentcore_control.types.default_stripe_privy_authorization_private_key_type
    import aws_sdk_bedrock_agentcore_control.types.secret_reference
    import aws_sdk_bedrock_agentcore_control.types.secret_source_type
    import aws_sdk_bedrock_agentcore_control.types.stripe_privy_app_id_type
    import aws_sdk_bedrock_agentcore_control.types.stripe_privy_authorization_id_type


class StripePrivyConfigurationInput(TypedDict, closed=True):
    app_id: "aws_sdk_bedrock_agentcore_control.types.stripe_privy_app_id_type.StripePrivyAppIdType"
    """<p>The app ID provided by Privy.</p>"""
    app_secret: "aws_sdk_bedrock_agentcore_control.types.default_stripe_privy_app_secret_type.DefaultStripePrivyAppSecretType"
    """<p>The app secret provided by Privy.</p>"""
    app_secret_source: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the app secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in AWS Secrets Manager.</p>"""
    app_secret_config: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_reference.SecretReference"
    ]
    """<p>A reference to the AWS Secrets Manager secret that stores the app secret. This includes the secret ID and the JSON key used to extract the app secret value from the secret. Required when <code>appSecretSource</code> is set to <code>EXTERNAL</code>.</p>"""
    authorization_private_key: "aws_sdk_bedrock_agentcore_control.types.default_stripe_privy_authorization_private_key_type.DefaultStripePrivyAuthorizationPrivateKeyType"
    """<p>The authorization private key for the Stripe Privy integration.</p>"""
    authorization_private_key_source: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
    ]
    """<p>The source type of the authorization private key. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in AWS Secrets Manager.</p>"""
    authorization_private_key_config: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.secret_reference.SecretReference"
    ]
    """<p>A reference to the AWS Secrets Manager secret that stores the authorization private key. This includes the secret ID and the JSON key used to extract the authorization private key value from the secret. Required when <code>authorizationPrivateKeySource</code> is set to <code>EXTERNAL</code>.</p>"""
    authorization_id: "aws_sdk_bedrock_agentcore_control.types.stripe_privy_authorization_id_type.StripePrivyAuthorizationIdType"
    """<p>The authorization ID for the Stripe Privy integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StripePrivyConfigurationInput) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["appSecret"] = value.get("app_secret", "")
    if "app_secret_source" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["appSecretSource"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["app_secret_source"]
            )
        )
    if "app_secret_config" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_reference

        out["appSecretConfig"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_reference.serialize_json(
                value["app_secret_config"]
            )
        )
    out["authorizationPrivateKey"] = value.get("authorization_private_key", "")
    if "authorization_private_key_source" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["authorizationPrivateKeySource"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.serialize_json(
                value["authorization_private_key_source"]
            )
        )
    if "authorization_private_key_config" in value:
        import aws_sdk_bedrock_agentcore_control.types.secret_reference

        out["authorizationPrivateKeyConfig"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_reference.serialize_json(
                value["authorization_private_key_config"]
            )
        )
    out["authorizationId"] = value["authorization_id"]
    return out


def deserialize_json(data: dict) -> StripePrivyConfigurationInput:
    out: StripePrivyConfigurationInput = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("StripePrivyConfigurationInput.app_id required")
    if "appSecret" in data:
        out["app_secret"] = data["appSecret"]
    else:
        out["app_secret"] = ""
    if "appSecretSource" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["app_secret_source"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["appSecretSource"]
            )
        )
    if "appSecretConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_reference

        out["app_secret_config"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_reference.deserialize_json(
                data["appSecretConfig"]
            )
        )
    if "authorizationPrivateKey" in data:
        out["authorization_private_key"] = data["authorizationPrivateKey"]
    else:
        out["authorization_private_key"] = ""
    if "authorizationPrivateKeySource" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_source_type

        out["authorization_private_key_source"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_source_type.deserialize_json(
                data["authorizationPrivateKeySource"]
            )
        )
    if "authorizationPrivateKeyConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.secret_reference

        out["authorization_private_key_config"] = (
            aws_sdk_bedrock_agentcore_control.types.secret_reference.deserialize_json(
                data["authorizationPrivateKeyConfig"]
            )
        )
    if "authorizationId" in data:
        out["authorization_id"] = data["authorizationId"]
    else:
        raise DeserializationError(
            "StripePrivyConfigurationInput.authorization_id required"
        )
    return out
