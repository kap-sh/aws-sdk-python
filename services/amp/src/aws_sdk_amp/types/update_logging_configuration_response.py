"""Generated from Smithy shape ``com.amazonaws.amp#UpdateLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.logging_configuration_status


class UpdateLoggingConfigurationResponse(TypedDict, closed=True):
    status: "aws_sdk_amp.types.logging_configuration_status.LoggingConfigurationStatus"
    """<p>A structure that contains the current status of the logging configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLoggingConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_amp.types.logging_configuration_status

    out["status"] = aws_sdk_amp.types.logging_configuration_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateLoggingConfigurationResponse:
    out: UpdateLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_amp.types.logging_configuration_status

        out["status"] = aws_sdk_amp.types.logging_configuration_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateLoggingConfigurationResponse.status required")
    return out
