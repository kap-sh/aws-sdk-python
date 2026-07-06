"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ResourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.open_search_resource_config


class _ResourceConfig_openSearchResourceConfig(TypedDict, closed=True):
    openSearchResourceConfig: "aws_sdk_cloudwatch_logs.types.open_search_resource_config.OpenSearchResourceConfig"


ResourceConfig: TypeAlias = _ResourceConfig_openSearchResourceConfig


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceConfig) -> dict:
    if "openSearchResourceConfig" in value:
        import aws_sdk_cloudwatch_logs.types.open_search_resource_config

        return {
            "openSearchResourceConfig": aws_sdk_cloudwatch_logs.types.open_search_resource_config.serialize_aws_json_1_1(
                value["openSearchResourceConfig"]
            )
        }
    else:
        raise SerializationError("ResourceConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ResourceConfig:
    if "openSearchResourceConfig" in data:
        import aws_sdk_cloudwatch_logs.types.open_search_resource_config

        return {
            "openSearchResourceConfig": aws_sdk_cloudwatch_logs.types.open_search_resource_config.deserialize_aws_json_1_1(
                data["openSearchResourceConfig"]
            )
        }
    else:
        raise DeserializationError("ResourceConfig: no recognized variant key")
