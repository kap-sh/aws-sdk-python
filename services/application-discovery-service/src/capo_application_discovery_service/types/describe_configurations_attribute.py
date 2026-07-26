"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeConfigurationsAttribute``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_discovery_service.types.string

DescribeConfigurationsAttribute: TypeAlias = dict[
    "capo_application_discovery_service.types.string.String",
    "capo_application_discovery_service.types.string.String",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: DescribeConfigurationsAttribute) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigurationsAttribute:
    out: DescribeConfigurationsAttribute = {}
    for key, value in data.items():
        out[key] = value
    return out
