"""Generated from Smithy shape ``com.amazonaws.sagemaker#IdentityProviderOAuthSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.identity_provider_o_auth_setting

IdentityProviderOAuthSettings: TypeAlias = list[
    "aws_sdk_sagemaker.types.identity_provider_o_auth_setting.IdentityProviderOAuthSetting"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityProviderOAuthSettings) -> list:
    import aws_sdk_sagemaker.types.identity_provider_o_auth_setting

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.identity_provider_o_auth_setting.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IdentityProviderOAuthSettings:
    import aws_sdk_sagemaker.types.identity_provider_o_auth_setting

    out: IdentityProviderOAuthSettings = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.identity_provider_o_auth_setting.deserialize_aws_json_1_1(
                item
            )
        )
    return out
