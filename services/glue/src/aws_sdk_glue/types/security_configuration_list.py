"""Generated from Smithy shape ``com.amazonaws.glue#SecurityConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.security_configuration

SecurityConfigurationList: TypeAlias = list[
    "aws_sdk_glue.types.security_configuration.SecurityConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityConfigurationList) -> list:
    import aws_sdk_glue.types.security_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.security_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SecurityConfigurationList:
    import aws_sdk_glue.types.security_configuration

    out: SecurityConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.security_configuration.deserialize_aws_json_1_1(item)
        )
    return out
