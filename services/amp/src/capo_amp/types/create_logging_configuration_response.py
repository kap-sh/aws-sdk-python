"""Generated from Smithy shape ``com.amazonaws.amp#CreateLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.logging_configuration_status


class CreateLoggingConfigurationResponse(TypedDict, closed=True):
    status: "capo_amp.types.logging_configuration_status.LoggingConfigurationStatus"
    """<p>A structure that displays the current status of the logging configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLoggingConfigurationResponse) -> dict:
    out: dict = {}
    import capo_amp.types.logging_configuration_status

    out["status"] = capo_amp.types.logging_configuration_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> CreateLoggingConfigurationResponse:
    out: CreateLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_amp.types.logging_configuration_status

        out["status"] = capo_amp.types.logging_configuration_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("CreateLoggingConfigurationResponse.status required")
    return out
