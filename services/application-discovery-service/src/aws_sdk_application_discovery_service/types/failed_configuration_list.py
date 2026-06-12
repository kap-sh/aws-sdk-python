"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#FailedConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.failed_configuration

FailedConfigurationList: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.failed_configuration.FailedConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedConfigurationList) -> list:
    import aws_sdk_application_discovery_service.types.failed_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_discovery_service.types.failed_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FailedConfigurationList:
    import aws_sdk_application_discovery_service.types.failed_configuration

    out: FailedConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_application_discovery_service.types.failed_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
