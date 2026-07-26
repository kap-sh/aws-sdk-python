"""Generated from Smithy shape ``com.amazonaws.kendra#UserTokenConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.user_token_configuration

UserTokenConfigurationList: TypeAlias = list[
    "capo_kendra.types.user_token_configuration.UserTokenConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserTokenConfigurationList) -> list:
    import capo_kendra.types.user_token_configuration

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.user_token_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UserTokenConfigurationList:
    import capo_kendra.types.user_token_configuration

    out: UserTokenConfigurationList = []
    for item in data:
        out.append(
            capo_kendra.types.user_token_configuration.deserialize_aws_json_1_1(item)
        )
    return out
