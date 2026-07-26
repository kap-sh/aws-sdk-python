"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#MFAOptionListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.mfa_option_type

MFAOptionListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.mfa_option_type.MFAOptionType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MFAOptionListType) -> list:
    import capo_cognito_identity_provider.types.mfa_option_type

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.mfa_option_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MFAOptionListType:
    import capo_cognito_identity_provider.types.mfa_option_type

    out: MFAOptionListType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.mfa_option_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
