"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ConfigurationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_discovery_service.types.configuration_id

ConfigurationIdList: TypeAlias = list[
    "capo_application_discovery_service.types.configuration_id.ConfigurationId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConfigurationIdList:
    return list(data)
