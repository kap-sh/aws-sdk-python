"""Generated from Smithy shape ``com.amazonaws.emrserverless#ConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.configuration

ConfigurationList: TypeAlias = list[
    "aws_sdk_emr_serverless.types.configuration.Configuration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationList) -> list:
    import aws_sdk_emr_serverless.types.configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_emr_serverless.types.configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConfigurationList:
    import aws_sdk_emr_serverless.types.configuration

    out: ConfigurationList = []
    for item in data:
        out.append(aws_sdk_emr_serverless.types.configuration.deserialize_json(item))
    return out
