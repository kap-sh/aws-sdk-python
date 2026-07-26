"""Generated from Smithy shape ``com.amazonaws.wisdom#SourceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_wisdom.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_wisdom.types.app_integrations_configuration


class _SourceConfiguration_appIntegrations(TypedDict, closed=True):
    appIntegrations: (
        "capo_wisdom.types.app_integrations_configuration.AppIntegrationsConfiguration"
    )


SourceConfiguration: TypeAlias = _SourceConfiguration_appIntegrations


# --- restJson1 ser/de ---
def serialize_json(value: SourceConfiguration) -> dict:
    if "appIntegrations" in value:
        import capo_wisdom.types.app_integrations_configuration

        return {
            "appIntegrations": capo_wisdom.types.app_integrations_configuration.serialize_json(
                value["appIntegrations"]
            )
        }
    else:
        raise SerializationError("SourceConfiguration: no variant present")


def deserialize_json(data: dict) -> SourceConfiguration:
    if "appIntegrations" in data:
        import capo_wisdom.types.app_integrations_configuration

        return {
            "appIntegrations": capo_wisdom.types.app_integrations_configuration.deserialize_json(
                data["appIntegrations"]
            )
        }
    else:
        raise DeserializationError("SourceConfiguration: no recognized variant key")
