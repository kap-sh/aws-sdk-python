"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AllowedFirstAuthFactorsListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.auth_factor_type

AllowedFirstAuthFactorsListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.auth_factor_type.AuthFactorType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowedFirstAuthFactorsListType) -> list:
    import aws_sdk_cognito_identity_provider.types.auth_factor_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.auth_factor_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AllowedFirstAuthFactorsListType:
    import aws_sdk_cognito_identity_provider.types.auth_factor_type

    out: AllowedFirstAuthFactorsListType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.auth_factor_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
