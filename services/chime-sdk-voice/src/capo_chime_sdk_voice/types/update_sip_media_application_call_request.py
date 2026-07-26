"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateSipMediaApplicationCallRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.sma_update_call_arguments_map


class UpdateSipMediaApplicationCallRequest(TypedDict, closed=True):
    sip_media_application_id: (
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The ID of the SIP media application handling the call.</p>"""
    transaction_id: "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    """<p>The ID of the call transaction.</p>"""
    arguments: "capo_chime_sdk_voice.types.sma_update_call_arguments_map.SMAUpdateCallArgumentsMap"
    """<p>Arguments made available to the Lambda function as part of the <code>CALL_UPDATE_REQUESTED</code> event. Can contain 0-20 key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSipMediaApplicationCallRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_voice.types.sma_update_call_arguments_map

    out["Arguments"] = (
        capo_chime_sdk_voice.types.sma_update_call_arguments_map.serialize_json(
            value["arguments"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateSipMediaApplicationCallRequest:
    out: UpdateSipMediaApplicationCallRequest = {}  # type: ignore[typeddict-item]
    if "Arguments" in data:
        import capo_chime_sdk_voice.types.sma_update_call_arguments_map

        out["arguments"] = (
            capo_chime_sdk_voice.types.sma_update_call_arguments_map.deserialize_json(
                data["Arguments"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateSipMediaApplicationCallRequest.arguments required"
        )
    return out
