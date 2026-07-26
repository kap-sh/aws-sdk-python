"""Generated from Smithy shape ``com.amazonaws.securitylake#LogSourceResource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securitylake.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_securitylake.types.aws_log_source_resource
    import capo_securitylake.types.custom_log_source_resource


class _LogSourceResource_awsLogSource(TypedDict, closed=True):
    awsLogSource: "capo_securitylake.types.aws_log_source_resource.AwsLogSourceResource"


class _LogSourceResource_customLogSource(TypedDict, closed=True):
    customLogSource: (
        "capo_securitylake.types.custom_log_source_resource.CustomLogSourceResource"
    )


LogSourceResource: TypeAlias = (
    _LogSourceResource_awsLogSource | _LogSourceResource_customLogSource
)


# --- restJson1 ser/de ---
def serialize_json(value: LogSourceResource) -> dict:
    if "awsLogSource" in value:
        import capo_securitylake.types.aws_log_source_resource

        return {
            "awsLogSource": capo_securitylake.types.aws_log_source_resource.serialize_json(
                value["awsLogSource"]
            )
        }
    elif "customLogSource" in value:
        import capo_securitylake.types.custom_log_source_resource

        return {
            "customLogSource": capo_securitylake.types.custom_log_source_resource.serialize_json(
                value["customLogSource"]
            )
        }
    else:
        raise SerializationError("LogSourceResource: no variant present")


def deserialize_json(data: dict) -> LogSourceResource:
    if "awsLogSource" in data:
        import capo_securitylake.types.aws_log_source_resource

        return {
            "awsLogSource": capo_securitylake.types.aws_log_source_resource.deserialize_json(
                data["awsLogSource"]
            )
        }
    elif "customLogSource" in data:
        import capo_securitylake.types.custom_log_source_resource

        return {
            "customLogSource": capo_securitylake.types.custom_log_source_resource.deserialize_json(
                data["customLogSource"]
            )
        }
    else:
        raise DeserializationError("LogSourceResource: no recognized variant key")
