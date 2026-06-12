"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#Configurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.configuration

Configurations: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.configuration.Configuration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Configurations) -> list:
    import aws_sdk_application_discovery_service.types.configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_discovery_service.types.configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Configurations:
    import aws_sdk_application_discovery_service.types.configuration

    out: Configurations = []
    for item in data:
        out.append(
            aws_sdk_application_discovery_service.types.configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
