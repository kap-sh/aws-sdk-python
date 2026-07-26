"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#GetNotificationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.notification_configuration


class GetNotificationConfigurationResponse(TypedDict, closed=True):
    notification_configuration: "capo_codeguruprofiler.types.notification_configuration.NotificationConfiguration"
    """<p>The current notification configuration for this profiling group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotificationConfigurationResponse) -> dict:
    out: dict = {}
    import capo_codeguruprofiler.types.notification_configuration

    out["notificationConfiguration"] = (
        capo_codeguruprofiler.types.notification_configuration.serialize_json(
            value["notification_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetNotificationConfigurationResponse:
    out: GetNotificationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "notificationConfiguration" in data:
        import capo_codeguruprofiler.types.notification_configuration

        out["notification_configuration"] = (
            capo_codeguruprofiler.types.notification_configuration.deserialize_json(
                data["notificationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetNotificationConfigurationResponse.notification_configuration required"
        )
    return out
