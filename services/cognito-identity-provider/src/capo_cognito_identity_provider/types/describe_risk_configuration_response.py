"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeRiskConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.risk_configuration_type


class DescribeRiskConfigurationResponse(TypedDict, closed=True):
    risk_configuration: "capo_cognito_identity_provider.types.risk_configuration_type.RiskConfigurationType"
    """<p>The details of the requested risk configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRiskConfigurationResponse) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.risk_configuration_type

    out["RiskConfiguration"] = (
        capo_cognito_identity_provider.types.risk_configuration_type.serialize_aws_json_1_1(
            value["risk_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRiskConfigurationResponse:
    out: DescribeRiskConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "RiskConfiguration" in data:
        import capo_cognito_identity_provider.types.risk_configuration_type

        out["risk_configuration"] = (
            capo_cognito_identity_provider.types.risk_configuration_type.deserialize_aws_json_1_1(
                data["RiskConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeRiskConfigurationResponse.risk_configuration required"
        )
    return out
