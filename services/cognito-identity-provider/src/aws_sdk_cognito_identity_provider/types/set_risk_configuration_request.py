"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetRiskConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.account_takeover_risk_configuration_type
    import aws_sdk_cognito_identity_provider.types.client_id_type
    import aws_sdk_cognito_identity_provider.types.compromised_credentials_risk_configuration_type
    import aws_sdk_cognito_identity_provider.types.risk_exception_configuration_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class SetRiskConfigurationRequest(TypedDict):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to set a risk configuration. If you include <code>UserPoolId</code> in your request, don't include <code>ClientId</code>. When the client ID is null, the same risk configuration is applied to all the clients in the userPool. When you include both <code>ClientId</code> and <code>UserPoolId</code>, Amazon Cognito maps the configuration to the app client only.</p>"""
    client_id: NotRequired[
        "aws_sdk_cognito_identity_provider.types.client_id_type.ClientIdType"
    ]
    """<p>The ID of the app client where you want to set a risk configuration. If <code>ClientId</code> is null, then the risk configuration is mapped to <code>UserPoolId</code>. When the client ID is null, the same risk configuration is applied to all the clients in the userPool.</p> <p>When you include a <code>ClientId</code> parameter, Amazon Cognito maps the configuration to the app client. When you include both <code>ClientId</code> and <code>UserPoolId</code>, Amazon Cognito maps the configuration to the app client only.</p>"""
    compromised_credentials_risk_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.compromised_credentials_risk_configuration_type.CompromisedCredentialsRiskConfigurationType"
    ]
    """<p>The configuration of automated reactions to detected compromised credentials. Includes settings for blocking future sign-in requests and for the types of password-submission events you want to monitor.</p>"""
    account_takeover_risk_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.account_takeover_risk_configuration_type.AccountTakeoverRiskConfigurationType"
    ]
    """<p>The settings for automated responses and notification templates for adaptive authentication with threat protection.</p>"""
    risk_exception_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.risk_exception_configuration_type.RiskExceptionConfigurationType"
    ]
    """<p>A set of IP-address overrides to threat protection. You can set up IP-address always-block and always-allow lists.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetRiskConfigurationRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "compromised_credentials_risk_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.compromised_credentials_risk_configuration_type

        out["CompromisedCredentialsRiskConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.compromised_credentials_risk_configuration_type.serialize_aws_json_1_1(
                value["compromised_credentials_risk_configuration"]
            )
        )
    if "account_takeover_risk_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.account_takeover_risk_configuration_type

        out["AccountTakeoverRiskConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.account_takeover_risk_configuration_type.serialize_aws_json_1_1(
                value["account_takeover_risk_configuration"]
            )
        )
    if "risk_exception_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.risk_exception_configuration_type

        out["RiskExceptionConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.risk_exception_configuration_type.serialize_aws_json_1_1(
                value["risk_exception_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetRiskConfigurationRequest:
    out: SetRiskConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("SetRiskConfigurationRequest.user_pool_id required")
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    if "CompromisedCredentialsRiskConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.compromised_credentials_risk_configuration_type

        out["compromised_credentials_risk_configuration"] = (
            aws_sdk_cognito_identity_provider.types.compromised_credentials_risk_configuration_type.deserialize_aws_json_1_1(
                data["CompromisedCredentialsRiskConfiguration"]
            )
        )
    if "AccountTakeoverRiskConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.account_takeover_risk_configuration_type

        out["account_takeover_risk_configuration"] = (
            aws_sdk_cognito_identity_provider.types.account_takeover_risk_configuration_type.deserialize_aws_json_1_1(
                data["AccountTakeoverRiskConfiguration"]
            )
        )
    if "RiskExceptionConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.risk_exception_configuration_type

        out["risk_exception_configuration"] = (
            aws_sdk_cognito_identity_provider.types.risk_exception_configuration_type.deserialize_aws_json_1_1(
                data["RiskExceptionConfiguration"]
            )
        )
    return out
