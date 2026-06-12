"""Generated from Smithy shape ``com.amazonaws.iot#SetLoggingOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.logging_options_payload


class SetLoggingOptionsRequest(TypedDict):
    logging_options_payload: (
        "aws_sdk_iot.types.logging_options_payload.LoggingOptionsPayload"
    )
    """<p>The logging options payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetLoggingOptionsRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.logging_options_payload

    out["loggingOptionsPayload"] = (
        aws_sdk_iot.types.logging_options_payload.serialize_json(
            value["logging_options_payload"]
        )
    )
    return out


def deserialize_json(data: dict) -> SetLoggingOptionsRequest:
    out: SetLoggingOptionsRequest = {}  # type: ignore[typeddict-item]
    if "loggingOptionsPayload" in data:
        import aws_sdk_iot.types.logging_options_payload

        out["logging_options_payload"] = (
            aws_sdk_iot.types.logging_options_payload.deserialize_json(
                data["loggingOptionsPayload"]
            )
        )
    else:
        raise DeserializationError(
            "SetLoggingOptionsRequest.logging_options_payload required"
        )
    return out
