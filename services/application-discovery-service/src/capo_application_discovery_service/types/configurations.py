"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#Configurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_discovery_service.types.configuration

Configurations: TypeAlias = list[
    "capo_application_discovery_service.types.configuration.Configuration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Configurations) -> list:
    import capo_application_discovery_service.types.configuration

    out: list = []
    for item in value:
        out.append(
            capo_application_discovery_service.types.configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Configurations:
    import capo_application_discovery_service.types.configuration

    out: Configurations = []
    for item in data:
        out.append(
            capo_application_discovery_service.types.configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
