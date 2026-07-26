"""Generated from Smithy shape ``com.amazonaws.iot#SetLoggingOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.logging_options_payload


class SetLoggingOptionsRequest(TypedDict, closed=True):
    logging_options_payload: (
        "capo_iot.types.logging_options_payload.LoggingOptionsPayload"
    )
    """<p>The logging options payload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetLoggingOptionsRequest) -> dict:
    out: dict = {}
    import capo_iot.types.logging_options_payload

    out["loggingOptionsPayload"] = (
        capo_iot.types.logging_options_payload.serialize_json(
            value["logging_options_payload"]
        )
    )
    return out


def deserialize_json(data: dict) -> SetLoggingOptionsRequest:
    out: SetLoggingOptionsRequest = {}  # type: ignore[typeddict-item]
    if "loggingOptionsPayload" in data:
        import capo_iot.types.logging_options_payload

        out["logging_options_payload"] = (
            capo_iot.types.logging_options_payload.deserialize_json(
                data["loggingOptionsPayload"]
            )
        )
    else:
        raise DeserializationError(
            "SetLoggingOptionsRequest.logging_options_payload required"
        )
    return out
