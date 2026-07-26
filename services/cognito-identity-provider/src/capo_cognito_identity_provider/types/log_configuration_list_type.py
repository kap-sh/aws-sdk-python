"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#LogConfigurationListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.log_configuration_type

LogConfigurationListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.log_configuration_type.LogConfigurationType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogConfigurationListType) -> list:
    import capo_cognito_identity_provider.types.log_configuration_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.log_configuration_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LogConfigurationListType:
    import capo_cognito_identity_provider.types.log_configuration_type

    out: LogConfigurationListType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.log_configuration_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
