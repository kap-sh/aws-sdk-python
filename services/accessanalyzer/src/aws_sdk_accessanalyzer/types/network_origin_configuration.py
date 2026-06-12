"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#NetworkOriginConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.internet_configuration
    import aws_sdk_accessanalyzer.types.vpc_configuration


class _NetworkOriginConfiguration_vpcConfiguration(TypedDict):
    vpcConfiguration: "aws_sdk_accessanalyzer.types.vpc_configuration.VpcConfiguration"


class _NetworkOriginConfiguration_internetConfiguration(TypedDict):
    internetConfiguration: (
        "aws_sdk_accessanalyzer.types.internet_configuration.InternetConfiguration"
    )


NetworkOriginConfiguration: TypeAlias = (
    _NetworkOriginConfiguration_vpcConfiguration
    | _NetworkOriginConfiguration_internetConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: NetworkOriginConfiguration) -> dict:
    if "vpcConfiguration" in value:
        import aws_sdk_accessanalyzer.types.vpc_configuration

        return {
            "vpcConfiguration": aws_sdk_accessanalyzer.types.vpc_configuration.serialize_json(
                value["vpcConfiguration"]
            )
        }
    elif "internetConfiguration" in value:
        import aws_sdk_accessanalyzer.types.internet_configuration

        return {
            "internetConfiguration": aws_sdk_accessanalyzer.types.internet_configuration.serialize_json(
                value["internetConfiguration"]
            )
        }
    else:
        raise SerializationError("NetworkOriginConfiguration: no variant present")


def deserialize_json(data: dict) -> NetworkOriginConfiguration:
    if "vpcConfiguration" in data:
        import aws_sdk_accessanalyzer.types.vpc_configuration

        return {
            "vpcConfiguration": aws_sdk_accessanalyzer.types.vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        }
    elif "internetConfiguration" in data:
        import aws_sdk_accessanalyzer.types.internet_configuration

        return {
            "internetConfiguration": aws_sdk_accessanalyzer.types.internet_configuration.deserialize_json(
                data["internetConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "NetworkOriginConfiguration: no recognized variant key"
        )
