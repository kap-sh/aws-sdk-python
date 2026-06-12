"""Generated from Smithy shape ``com.amazonaws.kendra#BasicAuthenticationConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.basic_authentication_configuration

BasicAuthenticationConfigurationList: TypeAlias = list[
    "aws_sdk_kendra.types.basic_authentication_configuration.BasicAuthenticationConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BasicAuthenticationConfigurationList) -> list:
    import aws_sdk_kendra.types.basic_authentication_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.basic_authentication_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BasicAuthenticationConfigurationList:
    import aws_sdk_kendra.types.basic_authentication_configuration

    out: BasicAuthenticationConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.basic_authentication_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
