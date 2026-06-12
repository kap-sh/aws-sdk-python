"""Generated from Smithy shape ``com.amazonaws.emrserverless#SensitivePropertiesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.configuration_property_key
    import aws_sdk_emr_serverless.types.configuration_property_value

SensitivePropertiesMap: TypeAlias = dict[
    "aws_sdk_emr_serverless.types.configuration_property_key.ConfigurationPropertyKey",
    "aws_sdk_emr_serverless.types.configuration_property_value.ConfigurationPropertyValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SensitivePropertiesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> SensitivePropertiesMap:
    out: SensitivePropertiesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
