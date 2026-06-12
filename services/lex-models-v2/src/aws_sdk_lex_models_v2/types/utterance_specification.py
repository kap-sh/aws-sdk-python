"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.analytics_channel
    import aws_sdk_lex_models_v2.types.analytics_long_value
    import aws_sdk_lex_models_v2.types.analytics_modality
    import aws_sdk_lex_models_v2.types.analytics_session_id
    import aws_sdk_lex_models_v2.types.bot_alias_id
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.intent_state
    import aws_sdk_lex_models_v2.types.locale_id
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.numerical_bot_version
    import aws_sdk_lex_models_v2.types.string
    import aws_sdk_lex_models_v2.types.timestamp
    import aws_sdk_lex_models_v2.types.utterance_bot_responses
    import aws_sdk_lex_models_v2.types.utterance_understood


class UtteranceSpecification(TypedDict):
    bot_alias_id: NotRequired["aws_sdk_lex_models_v2.types.bot_alias_id.BotAliasId"]
    """<p>The identifier of the alias of the bot that the utterance was made to.</p>"""
    bot_version: NotRequired[
        "aws_sdk_lex_models_v2.types.numerical_bot_version.NumericalBotVersion"
    ]
    """<p>The version of the bot that the utterance was made to.</p>"""
    locale_id: NotRequired["aws_sdk_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale of the bot that the utterance was made to.</p>"""
    session_id: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_session_id.AnalyticsSessionId"
    ]
    """<p>The identifier of the session that the utterance was made in.</p>"""
    channel: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_channel.AnalyticsChannel"
    ]
    """<p>The channel that is integrated with the bot that the utterance was made to.</p>"""
    mode: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_modality.AnalyticsModality"
    ]
    """<p>The mode of the session. The possible values are as follows:</p> <ul> <li> <p> <code>Speech</code> – The session consisted of spoken dialogue.</p> </li> <li> <p> <code>Text</code> – The session consisted of written dialogue.</p> </li> <li> <p> <code>DTMF</code> – The session consisted of touch-tone keypad (Dual Tone Multi-Frequency) key presses.</p> </li> <li> <p> <code>MultiMode</code> – The session consisted of multiple modes.</p> </li> </ul>"""
    conversation_start_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the conversation in which the utterance took place began. A conversation is defined as a unique combination of a <code>sessionId</code> and an <code>originatingRequestId</code>.</p>"""
    conversation_end_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The date and time when the conversation in which the utterance took place ended. A conversation is defined as a unique combination of a <code>sessionId</code> and an <code>originatingRequestId</code>.</p>"""
    utterance: NotRequired["aws_sdk_lex_models_v2.types.string.String"]
    """<p>The text of the utterance.</p>"""
    utterance_timestamp: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time when the utterance took place.</p>"""
    audio_voice_duration_millis: NotRequired[
        "aws_sdk_lex_models_v2.types.analytics_long_value.AnalyticsLongValue"
    ]
    """<p>The duration in milliseconds of the audio associated with the utterance.</p>"""
    utterance_understood: (
        "aws_sdk_lex_models_v2.types.utterance_understood.UtteranceUnderstood"
    )
    """<p>Specifies whether the bot understood the utterance or not.</p>"""
    input_type: NotRequired["aws_sdk_lex_models_v2.types.string.String"]
    """<p>The input type of the utterance. The possible values are as follows:</p> <ul> <li> <p>PCM format: audio data must be in little-endian byte order.</p> <ul> <li> <p> <code>audio/l16; rate=16000; channels=1</code> </p> </li> <li> <p> <code>audio/x-l16; sample-rate=16000; channel-count=1</code> </p> </li> <li> <p> <code>audio/lpcm; sample-rate=8000; sample-size-bits=16; channel-count=1; is-big-endian=false</code> </p> </li> </ul> </li> <li> <p>Opus format</p> <ul> <li> <p> <code>audio/x-cbr-opus-with-preamble;preamble-size=0;bit-rate=256000;frame-size-milliseconds=4</code> </p> </li> </ul> </li> <li> <p>Text format</p> <ul> <li> <p> <code>text/plain; charset=utf-8</code> </p> </li> </ul> </li> </ul>"""
    output_type: NotRequired["aws_sdk_lex_models_v2.types.string.String"]
    """<p>The output type of the utterance. The possible values are as follows:</p> <ul> <li> <p> <code>audio/mpeg</code> </p> </li> <li> <p> <code>audio/ogg</code> </p> </li> <li> <p> <code>audio/pcm (16 KHz)</code> </p> </li> <li> <p> <code>audio/</code> (defaults to <code>mpeg</code>)</p> </li> <li> <p> <code>text/plain; charset=utf-8</code> </p> </li> </ul>"""
    associated_intent_name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The name of the intent that the utterance is associated to.</p>"""
    associated_slot_name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The name of the slot that the utterance is associated to.</p>"""
    intent_state: NotRequired["aws_sdk_lex_models_v2.types.intent_state.IntentState"]
    """<p>The state of the intent that the utterance is associated to.</p>"""
    dialog_action_type: NotRequired["aws_sdk_lex_models_v2.types.string.String"]
    """<p>The type of dialog action that the utterance is associated to. See the <code>type</code> field in <a href=\"https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_DialogAction.html\">DialogAction</a> for more information.</p>"""
    bot_response_audio_voice_id: NotRequired[
        "aws_sdk_lex_models_v2.types.string.String"
    ]
    """<p>The identifier for the audio of the bot response.</p>"""
    slots_filled_in_session: NotRequired["aws_sdk_lex_models_v2.types.string.String"]
    """<p>The slots that have been filled in the session by the time of the utterance.</p>"""
    utterance_request_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The identifier of the request associated with the utterance.</p>"""
    bot_responses: NotRequired[
        "aws_sdk_lex_models_v2.types.utterance_bot_responses.UtteranceBotResponses"
    ]
    """<p>A list of objects containing information about the bot response to the utterance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceSpecification) -> dict:
    out: dict = {}
    if "bot_alias_id" in value:
        out["botAliasId"] = value["bot_alias_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "channel" in value:
        out["channel"] = value["channel"]
    if "mode" in value:
        import aws_sdk_lex_models_v2.types.analytics_modality

        out["mode"] = aws_sdk_lex_models_v2.types.analytics_modality.serialize_json(
            value["mode"]
        )
    if "conversation_start_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["conversationStartTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["conversation_start_time"]
            )
        )
    if "conversation_end_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["conversationEndTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["conversation_end_time"]
            )
        )
    if "utterance" in value:
        out["utterance"] = value["utterance"]
    if "utterance_timestamp" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["utteranceTimestamp"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["utterance_timestamp"]
            )
        )
    if "audio_voice_duration_millis" in value:
        out["audioVoiceDurationMillis"] = value["audio_voice_duration_millis"]
    out["utteranceUnderstood"] = value.get("utterance_understood", False)
    if "input_type" in value:
        out["inputType"] = value["input_type"]
    if "output_type" in value:
        out["outputType"] = value["output_type"]
    if "associated_intent_name" in value:
        out["associatedIntentName"] = value["associated_intent_name"]
    if "associated_slot_name" in value:
        out["associatedSlotName"] = value["associated_slot_name"]
    if "intent_state" in value:
        import aws_sdk_lex_models_v2.types.intent_state

        out["intentState"] = aws_sdk_lex_models_v2.types.intent_state.serialize_json(
            value["intent_state"]
        )
    if "dialog_action_type" in value:
        out["dialogActionType"] = value["dialog_action_type"]
    if "bot_response_audio_voice_id" in value:
        out["botResponseAudioVoiceId"] = value["bot_response_audio_voice_id"]
    if "slots_filled_in_session" in value:
        out["slotsFilledInSession"] = value["slots_filled_in_session"]
    if "utterance_request_id" in value:
        out["utteranceRequestId"] = value["utterance_request_id"]
    if "bot_responses" in value:
        import aws_sdk_lex_models_v2.types.utterance_bot_responses

        out["botResponses"] = (
            aws_sdk_lex_models_v2.types.utterance_bot_responses.serialize_json(
                value["bot_responses"]
            )
        )
    return out


def deserialize_json(data: dict) -> UtteranceSpecification:
    out: UtteranceSpecification = {}  # type: ignore[typeddict-item]
    if "botAliasId" in data:
        out["bot_alias_id"] = data["botAliasId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "channel" in data:
        out["channel"] = data["channel"]
    if "mode" in data:
        import aws_sdk_lex_models_v2.types.analytics_modality

        out["mode"] = aws_sdk_lex_models_v2.types.analytics_modality.deserialize_json(
            data["mode"]
        )
    if "conversationStartTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["conversation_start_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["conversationStartTime"]
            )
        )
    if "conversationEndTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["conversation_end_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["conversationEndTime"]
            )
        )
    if "utterance" in data:
        out["utterance"] = data["utterance"]
    if "utteranceTimestamp" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["utterance_timestamp"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["utteranceTimestamp"]
            )
        )
    if "audioVoiceDurationMillis" in data:
        out["audio_voice_duration_millis"] = data["audioVoiceDurationMillis"]
    if "utteranceUnderstood" in data:
        out["utterance_understood"] = data["utteranceUnderstood"]
    else:
        out["utterance_understood"] = False
    if "inputType" in data:
        out["input_type"] = data["inputType"]
    if "outputType" in data:
        out["output_type"] = data["outputType"]
    if "associatedIntentName" in data:
        out["associated_intent_name"] = data["associatedIntentName"]
    if "associatedSlotName" in data:
        out["associated_slot_name"] = data["associatedSlotName"]
    if "intentState" in data:
        import aws_sdk_lex_models_v2.types.intent_state

        out["intent_state"] = aws_sdk_lex_models_v2.types.intent_state.deserialize_json(
            data["intentState"]
        )
    if "dialogActionType" in data:
        out["dialog_action_type"] = data["dialogActionType"]
    if "botResponseAudioVoiceId" in data:
        out["bot_response_audio_voice_id"] = data["botResponseAudioVoiceId"]
    if "slotsFilledInSession" in data:
        out["slots_filled_in_session"] = data["slotsFilledInSession"]
    if "utteranceRequestId" in data:
        out["utterance_request_id"] = data["utteranceRequestId"]
    if "botResponses" in data:
        import aws_sdk_lex_models_v2.types.utterance_bot_responses

        out["bot_responses"] = (
            aws_sdk_lex_models_v2.types.utterance_bot_responses.deserialize_json(
                data["botResponses"]
            )
        )
    return out
