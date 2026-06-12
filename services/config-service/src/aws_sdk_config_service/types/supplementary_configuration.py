"""Generated from Smithy shape ``com.amazonaws.configservice#SupplementaryConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.supplementary_configuration_name
    import aws_sdk_config_service.types.supplementary_configuration_value

SupplementaryConfiguration: TypeAlias = dict[
    "aws_sdk_config_service.types.supplementary_configuration_name.SupplementaryConfigurationName",
    "aws_sdk_config_service.types.supplementary_configuration_value.SupplementaryConfigurationValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: SupplementaryConfiguration) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> SupplementaryConfiguration:
    out: SupplementaryConfiguration = {}
    for key, value in data.items():
        out[key] = value
    return out
