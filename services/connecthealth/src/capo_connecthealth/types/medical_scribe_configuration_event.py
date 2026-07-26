"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeConfigurationEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connecthealth._protocol.eventstream import HeaderValue, Message
from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connecthealth.types.encounter_context
    import capo_connecthealth.types.medical_scribe_channel_definitions
    import capo_connecthealth.types.medical_scribe_post_stream_action_settings


class MedicalScribeConfigurationEvent(TypedDict, closed=True):
    post_stream_action_settings: "capo_connecthealth.types.medical_scribe_post_stream_action_settings.MedicalScribePostStreamActionSettings"
    """<p>Settings for actions to perform after the stream ends</p>"""
    channel_definitions: NotRequired[
        "capo_connecthealth.types.medical_scribe_channel_definitions.MedicalScribeChannelDefinitions"
    ]
    """<p>Channel definitions for the audio stream</p>"""
    encounter_context: NotRequired[
        "capo_connecthealth.types.encounter_context.EncounterContext"
    ]
    """<p>Context information about the clinical encounter</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeConfigurationEvent) -> dict:
    out: dict = {}
    import capo_connecthealth.types.medical_scribe_post_stream_action_settings

    out["postStreamActionSettings"] = (
        capo_connecthealth.types.medical_scribe_post_stream_action_settings.serialize_json(
            value["post_stream_action_settings"]
        )
    )
    if "channel_definitions" in value:
        import capo_connecthealth.types.medical_scribe_channel_definitions

        out["channelDefinitions"] = (
            capo_connecthealth.types.medical_scribe_channel_definitions.serialize_json(
                value["channel_definitions"]
            )
        )
    if "encounter_context" in value:
        import capo_connecthealth.types.encounter_context

        out["encounterContext"] = (
            capo_connecthealth.types.encounter_context.serialize_json(
                value["encounter_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribeConfigurationEvent:
    out: MedicalScribeConfigurationEvent = {}  # type: ignore[typeddict-item]
    if "postStreamActionSettings" in data:
        import capo_connecthealth.types.medical_scribe_post_stream_action_settings

        out["post_stream_action_settings"] = (
            capo_connecthealth.types.medical_scribe_post_stream_action_settings.deserialize_json(
                data["postStreamActionSettings"]
            )
        )
    else:
        raise DeserializationError(
            "MedicalScribeConfigurationEvent.post_stream_action_settings required"
        )
    if "channelDefinitions" in data:
        import capo_connecthealth.types.medical_scribe_channel_definitions

        out["channel_definitions"] = (
            capo_connecthealth.types.medical_scribe_channel_definitions.deserialize_json(
                data["channelDefinitions"]
            )
        )
    if "encounterContext" in data:
        import capo_connecthealth.types.encounter_context

        out["encounter_context"] = (
            capo_connecthealth.types.encounter_context.deserialize_json(
                data["encounterContext"]
            )
        )
    return out


def serialize_event_json(value: MedicalScribeConfigurationEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "configurationEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> MedicalScribeConfigurationEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: MedicalScribeConfigurationEvent = {}  # type: ignore[typeddict-item]
    return out
