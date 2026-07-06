"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MaintenanceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.default_maintenance_configuration
    import aws_sdk_mediaconnect.types.preferred_day_time_maintenance_configuration


class _MaintenanceConfiguration_PreferredDayTime(TypedDict, closed=True):
    PreferredDayTime: "aws_sdk_mediaconnect.types.preferred_day_time_maintenance_configuration.PreferredDayTimeMaintenanceConfiguration"


class _MaintenanceConfiguration_Default(TypedDict, closed=True):
    Default: "aws_sdk_mediaconnect.types.default_maintenance_configuration.DefaultMaintenanceConfiguration"


MaintenanceConfiguration: TypeAlias = (
    _MaintenanceConfiguration_PreferredDayTime | _MaintenanceConfiguration_Default
)


# --- restJson1 ser/de ---
def serialize_json(value: MaintenanceConfiguration) -> dict:
    if "PreferredDayTime" in value:
        import aws_sdk_mediaconnect.types.preferred_day_time_maintenance_configuration

        return {
            "preferredDayTime": aws_sdk_mediaconnect.types.preferred_day_time_maintenance_configuration.serialize_json(
                value["PreferredDayTime"]
            )
        }
    elif "Default" in value:
        import aws_sdk_mediaconnect.types.default_maintenance_configuration

        return {
            "default": aws_sdk_mediaconnect.types.default_maintenance_configuration.serialize_json(
                value["Default"]
            )
        }
    else:
        raise SerializationError("MaintenanceConfiguration: no variant present")


def deserialize_json(data: dict) -> MaintenanceConfiguration:
    if "preferredDayTime" in data:
        import aws_sdk_mediaconnect.types.preferred_day_time_maintenance_configuration

        return {
            "PreferredDayTime": aws_sdk_mediaconnect.types.preferred_day_time_maintenance_configuration.deserialize_json(
                data["preferredDayTime"]
            )
        }
    elif "default" in data:
        import aws_sdk_mediaconnect.types.default_maintenance_configuration

        return {
            "Default": aws_sdk_mediaconnect.types.default_maintenance_configuration.deserialize_json(
                data["default"]
            )
        }
    else:
        raise DeserializationError(
            "MaintenanceConfiguration: no recognized variant key"
        )
