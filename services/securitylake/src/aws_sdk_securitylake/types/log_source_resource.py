"""Generated from Smithy shape ``com.amazonaws.securitylake#LogSourceResource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_securitylake.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.aws_log_source_resource
    import aws_sdk_securitylake.types.custom_log_source_resource


class _LogSourceResource_awsLogSource(TypedDict, closed=True):
    awsLogSource: (
        "aws_sdk_securitylake.types.aws_log_source_resource.AwsLogSourceResource"
    )


class _LogSourceResource_customLogSource(TypedDict, closed=True):
    customLogSource: (
        "aws_sdk_securitylake.types.custom_log_source_resource.CustomLogSourceResource"
    )


LogSourceResource: TypeAlias = (
    _LogSourceResource_awsLogSource | _LogSourceResource_customLogSource
)


# --- restJson1 ser/de ---
def serialize_json(value: LogSourceResource) -> dict:
    if "awsLogSource" in value:
        import aws_sdk_securitylake.types.aws_log_source_resource

        return {
            "awsLogSource": aws_sdk_securitylake.types.aws_log_source_resource.serialize_json(
                value["awsLogSource"]
            )
        }
    elif "customLogSource" in value:
        import aws_sdk_securitylake.types.custom_log_source_resource

        return {
            "customLogSource": aws_sdk_securitylake.types.custom_log_source_resource.serialize_json(
                value["customLogSource"]
            )
        }
    else:
        raise SerializationError("LogSourceResource: no variant present")


def deserialize_json(data: dict) -> LogSourceResource:
    if "awsLogSource" in data:
        import aws_sdk_securitylake.types.aws_log_source_resource

        return {
            "awsLogSource": aws_sdk_securitylake.types.aws_log_source_resource.deserialize_json(
                data["awsLogSource"]
            )
        }
    elif "customLogSource" in data:
        import aws_sdk_securitylake.types.custom_log_source_resource

        return {
            "customLogSource": aws_sdk_securitylake.types.custom_log_source_resource.deserialize_json(
                data["customLogSource"]
            )
        }
    else:
        raise DeserializationError("LogSourceResource: no recognized variant key")
