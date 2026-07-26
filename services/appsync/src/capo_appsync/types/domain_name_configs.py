"""Generated from Smithy shape ``com.amazonaws.appsync#DomainNameConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appsync.types.domain_name_config

DomainNameConfigs: TypeAlias = list[
    "capo_appsync.types.domain_name_config.DomainNameConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainNameConfigs) -> list:
    import capo_appsync.types.domain_name_config

    out: list = []
    for item in value:
        out.append(capo_appsync.types.domain_name_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainNameConfigs:
    import capo_appsync.types.domain_name_config

    out: DomainNameConfigs = []
    for item in data:
        out.append(capo_appsync.types.domain_name_config.deserialize_json(item))
    return out
