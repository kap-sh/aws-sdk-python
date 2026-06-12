"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ConfigurationTagSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.configuration_tag

ConfigurationTagSet: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.configuration_tag.ConfigurationTag"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationTagSet) -> list:
    import aws_sdk_application_discovery_service.types.configuration_tag

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_discovery_service.types.configuration_tag.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigurationTagSet:
    import aws_sdk_application_discovery_service.types.configuration_tag

    out: ConfigurationTagSet = []
    for item in data:
        out.append(
            aws_sdk_application_discovery_service.types.configuration_tag.deserialize_aws_json_1_1(
                item
            )
        )
    return out
