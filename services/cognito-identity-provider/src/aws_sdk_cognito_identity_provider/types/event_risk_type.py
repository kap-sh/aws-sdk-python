"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EventRiskType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.risk_decision_type
    import aws_sdk_cognito_identity_provider.types.risk_level_type
    import aws_sdk_cognito_identity_provider.types.wrapped_boolean_type


class EventRiskType(TypedDict):
    risk_decision: NotRequired[
        "aws_sdk_cognito_identity_provider.types.risk_decision_type.RiskDecisionType"
    ]
    """<p>The action taken by adaptive authentication. If <code>NoRisk</code>, your user pool took no action. If <code>AccountTakeover</code>, your user pool applied the adaptive authentication automated response that you configured. If <code>Block</code>, your user pool prevented the attempt.</p>"""
    risk_level: NotRequired[
        "aws_sdk_cognito_identity_provider.types.risk_level_type.RiskLevelType"
    ]
    """<p>The risk level that adaptive authentication assessed for the authentication event.</p>"""
    compromised_credentials_detected: NotRequired[
        "aws_sdk_cognito_identity_provider.types.wrapped_boolean_type.WrappedBooleanType"
    ]
    """<p>Indicates whether compromised credentials were detected during an authentication event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventRiskType) -> dict:
    out: dict = {}
    if "risk_decision" in value:
        import aws_sdk_cognito_identity_provider.types.risk_decision_type

        out["RiskDecision"] = (
            aws_sdk_cognito_identity_provider.types.risk_decision_type.serialize_aws_json_1_1(
                value["risk_decision"]
            )
        )
    if "risk_level" in value:
        import aws_sdk_cognito_identity_provider.types.risk_level_type

        out["RiskLevel"] = (
            aws_sdk_cognito_identity_provider.types.risk_level_type.serialize_aws_json_1_1(
                value["risk_level"]
            )
        )
    if "compromised_credentials_detected" in value:
        out["CompromisedCredentialsDetected"] = value[
            "compromised_credentials_detected"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventRiskType:
    out: EventRiskType = {}  # type: ignore[typeddict-item]
    if "RiskDecision" in data:
        import aws_sdk_cognito_identity_provider.types.risk_decision_type

        out["risk_decision"] = (
            aws_sdk_cognito_identity_provider.types.risk_decision_type.deserialize_aws_json_1_1(
                data["RiskDecision"]
            )
        )
    if "RiskLevel" in data:
        import aws_sdk_cognito_identity_provider.types.risk_level_type

        out["risk_level"] = (
            aws_sdk_cognito_identity_provider.types.risk_level_type.deserialize_aws_json_1_1(
                data["RiskLevel"]
            )
        )
    if "CompromisedCredentialsDetected" in data:
        out["compromised_credentials_detected"] = data["CompromisedCredentialsDetected"]
    return out
