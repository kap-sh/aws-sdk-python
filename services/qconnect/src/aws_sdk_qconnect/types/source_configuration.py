"""Generated from Smithy shape ``com.amazonaws.qconnect#SourceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_qconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.app_integrations_configuration
    import aws_sdk_qconnect.types.managed_source_configuration


class _SourceConfiguration_appIntegrations(TypedDict):
    appIntegrations: "aws_sdk_qconnect.types.app_integrations_configuration.AppIntegrationsConfiguration"


class _SourceConfiguration_managedSourceConfiguration(TypedDict):
    managedSourceConfiguration: (
        "aws_sdk_qconnect.types.managed_source_configuration.ManagedSourceConfiguration"
    )


SourceConfiguration: TypeAlias = (
    _SourceConfiguration_appIntegrations
    | _SourceConfiguration_managedSourceConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: SourceConfiguration) -> dict:
    if "appIntegrations" in value:
        import aws_sdk_qconnect.types.app_integrations_configuration

        return {
            "appIntegrations": aws_sdk_qconnect.types.app_integrations_configuration.serialize_json(
                value["appIntegrations"]
            )
        }
    elif "managedSourceConfiguration" in value:
        import aws_sdk_qconnect.types.managed_source_configuration

        return {
            "managedSourceConfiguration": aws_sdk_qconnect.types.managed_source_configuration.serialize_json(
                value["managedSourceConfiguration"]
            )
        }
    else:
        raise SerializationError("SourceConfiguration: no variant present")


def deserialize_json(data: dict) -> SourceConfiguration:
    if "appIntegrations" in data:
        import aws_sdk_qconnect.types.app_integrations_configuration

        return {
            "appIntegrations": aws_sdk_qconnect.types.app_integrations_configuration.deserialize_json(
                data["appIntegrations"]
            )
        }
    elif "managedSourceConfiguration" in data:
        import aws_sdk_qconnect.types.managed_source_configuration

        return {
            "managedSourceConfiguration": aws_sdk_qconnect.types.managed_source_configuration.deserialize_json(
                data["managedSourceConfiguration"]
            )
        }
    else:
        raise DeserializationError("SourceConfiguration: no recognized variant key")
