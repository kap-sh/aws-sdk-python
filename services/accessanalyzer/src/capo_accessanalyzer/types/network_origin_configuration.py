"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#NetworkOriginConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.internet_configuration
    import capo_accessanalyzer.types.vpc_configuration


class _NetworkOriginConfiguration_vpcConfiguration(TypedDict, closed=True):
    vpcConfiguration: "capo_accessanalyzer.types.vpc_configuration.VpcConfiguration"


class _NetworkOriginConfiguration_internetConfiguration(TypedDict, closed=True):
    internetConfiguration: (
        "capo_accessanalyzer.types.internet_configuration.InternetConfiguration"
    )


NetworkOriginConfiguration: TypeAlias = (
    _NetworkOriginConfiguration_vpcConfiguration
    | _NetworkOriginConfiguration_internetConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: NetworkOriginConfiguration) -> dict:
    if "vpcConfiguration" in value:
        import capo_accessanalyzer.types.vpc_configuration

        return {
            "vpcConfiguration": capo_accessanalyzer.types.vpc_configuration.serialize_json(
                value["vpcConfiguration"]
            )
        }
    elif "internetConfiguration" in value:
        import capo_accessanalyzer.types.internet_configuration

        return {
            "internetConfiguration": capo_accessanalyzer.types.internet_configuration.serialize_json(
                value["internetConfiguration"]
            )
        }
    else:
        raise SerializationError("NetworkOriginConfiguration: no variant present")


def deserialize_json(data: dict) -> NetworkOriginConfiguration:
    if "vpcConfiguration" in data:
        import capo_accessanalyzer.types.vpc_configuration

        return {
            "vpcConfiguration": capo_accessanalyzer.types.vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        }
    elif "internetConfiguration" in data:
        import capo_accessanalyzer.types.internet_configuration

        return {
            "internetConfiguration": capo_accessanalyzer.types.internet_configuration.deserialize_json(
                data["internetConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "NetworkOriginConfiguration: no recognized variant key"
        )
