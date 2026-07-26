"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeConfigurationsAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_discovery_service.types.describe_configurations_attribute

DescribeConfigurationsAttributes: TypeAlias = list[
    "capo_application_discovery_service.types.describe_configurations_attribute.DescribeConfigurationsAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigurationsAttributes) -> list:
    import capo_application_discovery_service.types.describe_configurations_attribute

    out: list = []
    for item in value:
        out.append(
            capo_application_discovery_service.types.describe_configurations_attribute.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DescribeConfigurationsAttributes:
    import capo_application_discovery_service.types.describe_configurations_attribute

    out: DescribeConfigurationsAttributes = []
    for item in data:
        out.append(
            capo_application_discovery_service.types.describe_configurations_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out
