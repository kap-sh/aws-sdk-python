"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetRiskConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.risk_configuration_type


class SetRiskConfigurationResponse(TypedDict):
    risk_configuration: "aws_sdk_cognito_identity_provider.types.risk_configuration_type.RiskConfigurationType"
    """<p>The API response that contains the risk configuration that you set and the timestamp of the most recent change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetRiskConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity_provider.types.risk_configuration_type

    out["RiskConfiguration"] = (
        aws_sdk_cognito_identity_provider.types.risk_configuration_type.serialize_aws_json_1_1(
            value["risk_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetRiskConfigurationResponse:
    out: SetRiskConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "RiskConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.risk_configuration_type

        out["risk_configuration"] = (
            aws_sdk_cognito_identity_provider.types.risk_configuration_type.deserialize_aws_json_1_1(
                data["RiskConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "SetRiskConfigurationResponse.risk_configuration required"
        )
    return out
