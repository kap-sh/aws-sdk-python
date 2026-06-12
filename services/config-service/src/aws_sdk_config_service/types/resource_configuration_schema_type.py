"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceConfigurationSchemaType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

ResourceConfigurationSchemaType: TypeAlias = Literal["CFN_RESOURCE_SCHEMA",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CFN_RESOURCE_SCHEMA",))


def serialize_aws_json_1_1(value: ResourceConfigurationSchemaType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceConfigurationSchemaType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResourceConfigurationSchemaType value: {data!r}"
        )
    return cast(ResourceConfigurationSchemaType, data)
