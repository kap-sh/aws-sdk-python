"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ConfiguredUserAuthFactorsListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.auth_factor_type

ConfiguredUserAuthFactorsListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.auth_factor_type.AuthFactorType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfiguredUserAuthFactorsListType) -> list:
    import capo_cognito_identity_provider.types.auth_factor_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.auth_factor_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfiguredUserAuthFactorsListType:
    import capo_cognito_identity_provider.types.auth_factor_type

    out: ConfiguredUserAuthFactorsListType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.auth_factor_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
