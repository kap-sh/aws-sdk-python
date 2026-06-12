"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AnalyzerConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.internal_access_configuration
    import aws_sdk_accessanalyzer.types.unused_access_configuration


class _AnalyzerConfiguration_unusedAccess(TypedDict):
    unusedAccess: "aws_sdk_accessanalyzer.types.unused_access_configuration.UnusedAccessConfiguration"


class _AnalyzerConfiguration_internalAccess(TypedDict):
    internalAccess: "aws_sdk_accessanalyzer.types.internal_access_configuration.InternalAccessConfiguration"


AnalyzerConfiguration: TypeAlias = (
    _AnalyzerConfiguration_unusedAccess | _AnalyzerConfiguration_internalAccess
)


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzerConfiguration) -> dict:
    if "unusedAccess" in value:
        import aws_sdk_accessanalyzer.types.unused_access_configuration

        return {
            "unusedAccess": aws_sdk_accessanalyzer.types.unused_access_configuration.serialize_json(
                value["unusedAccess"]
            )
        }
    elif "internalAccess" in value:
        import aws_sdk_accessanalyzer.types.internal_access_configuration

        return {
            "internalAccess": aws_sdk_accessanalyzer.types.internal_access_configuration.serialize_json(
                value["internalAccess"]
            )
        }
    else:
        raise SerializationError("AnalyzerConfiguration: no variant present")


def deserialize_json(data: dict) -> AnalyzerConfiguration:
    if "unusedAccess" in data:
        import aws_sdk_accessanalyzer.types.unused_access_configuration

        return {
            "unusedAccess": aws_sdk_accessanalyzer.types.unused_access_configuration.deserialize_json(
                data["unusedAccess"]
            )
        }
    elif "internalAccess" in data:
        import aws_sdk_accessanalyzer.types.internal_access_configuration

        return {
            "internalAccess": aws_sdk_accessanalyzer.types.internal_access_configuration.deserialize_json(
                data["internalAccess"]
            )
        }
    else:
        raise DeserializationError("AnalyzerConfiguration: no recognized variant key")
