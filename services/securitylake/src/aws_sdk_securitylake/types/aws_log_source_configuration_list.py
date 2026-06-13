"""Generated from Smithy shape ``com.amazonaws.securitylake#AwsLogSourceConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.aws_log_source_configuration

AwsLogSourceConfigurationList: TypeAlias = list[
    "aws_sdk_securitylake.types.aws_log_source_configuration.AwsLogSourceConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsLogSourceConfigurationList) -> list:
    import aws_sdk_securitylake.types.aws_log_source_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securitylake.types.aws_log_source_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsLogSourceConfigurationList:
    import aws_sdk_securitylake.types.aws_log_source_configuration

    out: AwsLogSourceConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_securitylake.types.aws_log_source_configuration.deserialize_json(
                item
            )
        )
    return out
