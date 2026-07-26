"""Generated from Smithy shape ``com.amazonaws.securitylake#AwsLogSourceConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securitylake.types.aws_log_source_configuration

AwsLogSourceConfigurationList: TypeAlias = list[
    "capo_securitylake.types.aws_log_source_configuration.AwsLogSourceConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsLogSourceConfigurationList) -> list:
    import capo_securitylake.types.aws_log_source_configuration

    out: list = []
    for item in value:
        out.append(
            capo_securitylake.types.aws_log_source_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsLogSourceConfigurationList:
    import capo_securitylake.types.aws_log_source_configuration

    out: AwsLogSourceConfigurationList = []
    for item in data:
        out.append(
            capo_securitylake.types.aws_log_source_configuration.deserialize_json(item)
        )
    return out
