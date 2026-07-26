"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceConfigurationSchemaType``."""

from typing import Literal, TypeAlias, cast

ResourceConfigurationSchemaType: TypeAlias = Literal["CFN_RESOURCE_SCHEMA",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceConfigurationSchemaType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceConfigurationSchemaType:
    return cast(ResourceConfigurationSchemaType, data)
