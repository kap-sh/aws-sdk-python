"""Generated from Smithy shape ``com.amazonaws.amp#UpdateLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.logging_configuration_status


class UpdateLoggingConfigurationResponse(TypedDict, closed=True):
    status: "capo_amp.types.logging_configuration_status.LoggingConfigurationStatus"
    """<p>A structure that contains the current status of the logging configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLoggingConfigurationResponse) -> dict:
    out: dict = {}
    import capo_amp.types.logging_configuration_status

    out["status"] = capo_amp.types.logging_configuration_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateLoggingConfigurationResponse:
    out: UpdateLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_amp.types.logging_configuration_status

        out["status"] = capo_amp.types.logging_configuration_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateLoggingConfigurationResponse.status required")
    return out
