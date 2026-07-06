"""Generated from Smithy shape ``com.amazonaws.iotevents#PutLoggingOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.logging_options


class PutLoggingOptionsRequest(TypedDict, closed=True):
    logging_options: "aws_sdk_iot_events.types.logging_options.LoggingOptions"
    """<p>The new values of the AWS IoT Events logging options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutLoggingOptionsRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_events.types.logging_options

    out["loggingOptions"] = aws_sdk_iot_events.types.logging_options.serialize_json(
        value["logging_options"]
    )
    return out


def deserialize_json(data: dict) -> PutLoggingOptionsRequest:
    out: PutLoggingOptionsRequest = {}  # type: ignore[typeddict-item]
    if "loggingOptions" in data:
        import aws_sdk_iot_events.types.logging_options

        out["logging_options"] = (
            aws_sdk_iot_events.types.logging_options.deserialize_json(
                data["loggingOptions"]
            )
        )
    else:
        raise DeserializationError("PutLoggingOptionsRequest.logging_options required")
    return out
