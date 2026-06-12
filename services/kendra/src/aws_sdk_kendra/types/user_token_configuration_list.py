"""Generated from Smithy shape ``com.amazonaws.kendra#UserTokenConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.user_token_configuration

UserTokenConfigurationList: TypeAlias = list[
    "aws_sdk_kendra.types.user_token_configuration.UserTokenConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserTokenConfigurationList) -> list:
    import aws_sdk_kendra.types.user_token_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.user_token_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UserTokenConfigurationList:
    import aws_sdk_kendra.types.user_token_configuration

    out: UserTokenConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.user_token_configuration.deserialize_aws_json_1_1(item)
        )
    return out
