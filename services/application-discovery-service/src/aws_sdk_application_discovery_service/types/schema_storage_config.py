"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#SchemaStorageConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.database_name
    import aws_sdk_application_discovery_service.types.string

SchemaStorageConfig: TypeAlias = dict[
    "aws_sdk_application_discovery_service.types.database_name.DatabaseName",
    "aws_sdk_application_discovery_service.types.string.String",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: SchemaStorageConfig) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> SchemaStorageConfig:
    out: SchemaStorageConfig = {}
    for key, value in data.items():
        out[key] = value
    return out
