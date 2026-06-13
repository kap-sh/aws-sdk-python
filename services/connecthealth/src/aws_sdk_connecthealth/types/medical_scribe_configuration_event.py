"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeConfigurationEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.encounter_context
    import aws_sdk_connecthealth.types.medical_scribe_channel_definitions
    import aws_sdk_connecthealth.types.medical_scribe_post_stream_action_settings


class MedicalScribeConfigurationEvent(TypedDict):
    post_stream_action_settings: "aws_sdk_connecthealth.types.medical_scribe_post_stream_action_settings.MedicalScribePostStreamActionSettings"
    """<p>Settings for actions to perform after the stream ends</p>"""
    channel_definitions: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_channel_definitions.MedicalScribeChannelDefinitions"
    ]
    """<p>Channel definitions for the audio stream</p>"""
    encounter_context: NotRequired[
        "aws_sdk_connecthealth.types.encounter_context.EncounterContext"
    ]
    """<p>Context information about the clinical encounter</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeConfigurationEvent) -> dict:
    out: dict = {}
    import aws_sdk_connecthealth.types.medical_scribe_post_stream_action_settings

    out["postStreamActionSettings"] = (
        aws_sdk_connecthealth.types.medical_scribe_post_stream_action_settings.serialize_json(
            value["post_stream_action_settings"]
        )
    )
    if "channel_definitions" in value:
        import aws_sdk_connecthealth.types.medical_scribe_channel_definitions

        out["channelDefinitions"] = (
            aws_sdk_connecthealth.types.medical_scribe_channel_definitions.serialize_json(
                value["channel_definitions"]
            )
        )
    if "encounter_context" in value:
        import aws_sdk_connecthealth.types.encounter_context

        out["encounterContext"] = (
            aws_sdk_connecthealth.types.encounter_context.serialize_json(
                value["encounter_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribeConfigurationEvent:
    out: MedicalScribeConfigurationEvent = {}  # type: ignore[typeddict-item]
    if "postStreamActionSettings" in data:
        import aws_sdk_connecthealth.types.medical_scribe_post_stream_action_settings

        out["post_stream_action_settings"] = (
            aws_sdk_connecthealth.types.medical_scribe_post_stream_action_settings.deserialize_json(
                data["postStreamActionSettings"]
            )
        )
    else:
        raise DeserializationError(
            "MedicalScribeConfigurationEvent.post_stream_action_settings required"
        )
    if "channelDefinitions" in data:
        import aws_sdk_connecthealth.types.medical_scribe_channel_definitions

        out["channel_definitions"] = (
            aws_sdk_connecthealth.types.medical_scribe_channel_definitions.deserialize_json(
                data["channelDefinitions"]
            )
        )
    if "encounterContext" in data:
        import aws_sdk_connecthealth.types.encounter_context

        out["encounter_context"] = (
            aws_sdk_connecthealth.types.encounter_context.deserialize_json(
                data["encounterContext"]
            )
        )
    return out
