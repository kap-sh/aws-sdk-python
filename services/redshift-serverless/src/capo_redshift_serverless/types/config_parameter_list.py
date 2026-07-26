"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ConfigParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_serverless.types.config_parameter

ConfigParameterList: TypeAlias = list[
    "capo_redshift_serverless.types.config_parameter.ConfigParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigParameterList) -> list:
    import capo_redshift_serverless.types.config_parameter

    out: list = []
    for item in value:
        out.append(
            capo_redshift_serverless.types.config_parameter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigParameterList:
    import capo_redshift_serverless.types.config_parameter

    out: ConfigParameterList = []
    for item in data:
        out.append(
            capo_redshift_serverless.types.config_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
