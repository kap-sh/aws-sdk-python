"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeRiskConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.risk_configuration_type


class DescribeRiskConfigurationResponse(TypedDict):
    risk_configuration: "aws_sdk_cognito_identity_provider.types.risk_configuration_type.RiskConfigurationType"
    """<p>The details of the requested risk configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRiskConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity_provider.types.risk_configuration_type

    out["RiskConfiguration"] = (
        aws_sdk_cognito_identity_provider.types.risk_configuration_type.serialize_aws_json_1_1(
            value["risk_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRiskConfigurationResponse:
    out: DescribeRiskConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "RiskConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.risk_configuration_type

        out["risk_configuration"] = (
            aws_sdk_cognito_identity_provider.types.risk_configuration_type.deserialize_aws_json_1_1(
                data["RiskConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeRiskConfigurationResponse.risk_configuration required"
        )
    return out
