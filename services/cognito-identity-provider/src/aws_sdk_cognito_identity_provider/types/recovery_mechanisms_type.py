"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RecoveryMechanismsType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.recovery_option_type

RecoveryMechanismsType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.recovery_option_type.RecoveryOptionType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecoveryMechanismsType) -> list:
    import aws_sdk_cognito_identity_provider.types.recovery_option_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.recovery_option_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RecoveryMechanismsType:
    import aws_sdk_cognito_identity_provider.types.recovery_option_type

    out: RecoveryMechanismsType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.recovery_option_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
