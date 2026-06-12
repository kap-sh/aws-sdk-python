"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.configuration

ConfigurationList: TypeAlias = list[
    "aws_sdk_emr_containers.types.configuration.Configuration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationList) -> list:
    import aws_sdk_emr_containers.types.configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_emr_containers.types.configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConfigurationList:
    import aws_sdk_emr_containers.types.configuration

    out: ConfigurationList = []
    for item in data:
        out.append(aws_sdk_emr_containers.types.configuration.deserialize_json(item))
    return out
