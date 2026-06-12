"""Generated from Smithy shape ``com.amazonaws.appsync#DomainNameConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appsync.types.domain_name_config

DomainNameConfigs: TypeAlias = list[
    "aws_sdk_appsync.types.domain_name_config.DomainNameConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainNameConfigs) -> list:
    import aws_sdk_appsync.types.domain_name_config

    out: list = []
    for item in value:
        out.append(aws_sdk_appsync.types.domain_name_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainNameConfigs:
    import aws_sdk_appsync.types.domain_name_config

    out: DomainNameConfigs = []
    for item in data:
        out.append(aws_sdk_appsync.types.domain_name_config.deserialize_json(item))
    return out
