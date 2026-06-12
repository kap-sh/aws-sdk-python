"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolAddOnsType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.advanced_security_additional_flows_type
    import aws_sdk_cognito_identity_provider.types.advanced_security_mode_type


class UserPoolAddOnsType(TypedDict):
    advanced_security_mode: "aws_sdk_cognito_identity_provider.types.advanced_security_mode_type.AdvancedSecurityModeType"
    """<p>The operating mode of threat protection for standard authentication types in your user pool, including username-password and secure remote password (SRP) authentication. </p>"""
    advanced_security_additional_flows: NotRequired[
        "aws_sdk_cognito_identity_provider.types.advanced_security_additional_flows_type.AdvancedSecurityAdditionalFlowsType"
    ]
    """<p>Threat protection configuration options for additional authentication types in your user pool, including custom authentication. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolAddOnsType) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity_provider.types.advanced_security_mode_type

    out["AdvancedSecurityMode"] = (
        aws_sdk_cognito_identity_provider.types.advanced_security_mode_type.serialize_aws_json_1_1(
            value["advanced_security_mode"]
        )
    )
    if "advanced_security_additional_flows" in value:
        import aws_sdk_cognito_identity_provider.types.advanced_security_additional_flows_type

        out["AdvancedSecurityAdditionalFlows"] = (
            aws_sdk_cognito_identity_provider.types.advanced_security_additional_flows_type.serialize_aws_json_1_1(
                value["advanced_security_additional_flows"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserPoolAddOnsType:
    out: UserPoolAddOnsType = {}  # type: ignore[typeddict-item]
    if "AdvancedSecurityMode" in data:
        import aws_sdk_cognito_identity_provider.types.advanced_security_mode_type

        out["advanced_security_mode"] = (
            aws_sdk_cognito_identity_provider.types.advanced_security_mode_type.deserialize_aws_json_1_1(
                data["AdvancedSecurityMode"]
            )
        )
    else:
        raise DeserializationError("UserPoolAddOnsType.advanced_security_mode required")
    if "AdvancedSecurityAdditionalFlows" in data:
        import aws_sdk_cognito_identity_provider.types.advanced_security_additional_flows_type

        out["advanced_security_additional_flows"] = (
            aws_sdk_cognito_identity_provider.types.advanced_security_additional_flows_type.deserialize_aws_json_1_1(
                data["AdvancedSecurityAdditionalFlows"]
            )
        )
    return out
