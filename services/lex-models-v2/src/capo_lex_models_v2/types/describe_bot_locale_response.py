"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeBotLocaleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.audio_filler_settings
    import capo_lex_models_v2.types.bot_locale_history_events_list
    import capo_lex_models_v2.types.bot_locale_status
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.confidence_threshold
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.failure_reasons
    import capo_lex_models_v2.types.generative_ai_settings
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.locale_name
    import capo_lex_models_v2.types.recommended_actions
    import capo_lex_models_v2.types.resource_count
    import capo_lex_models_v2.types.speech_detection_sensitivity
    import capo_lex_models_v2.types.speech_recognition_settings
    import capo_lex_models_v2.types.timestamp
    import capo_lex_models_v2.types.unified_speech_settings
    import capo_lex_models_v2.types.voice_settings


class DescribeBotLocaleResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot associated with the locale.</p>"""
    bot_version: NotRequired["capo_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The version of the bot associated with the locale.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The unique identifier of the described locale.</p>"""
    locale_name: NotRequired["capo_lex_models_v2.types.locale_name.LocaleName"]
    """<p>The name of the locale.</p>"""
    description: NotRequired["capo_lex_models_v2.types.description.Description"]
    """<p>The description of the locale.</p>"""
    nlu_intent_confidence_threshold: NotRequired[
        "capo_lex_models_v2.types.confidence_threshold.ConfidenceThreshold"
    ]
    """<p>The confidence threshold where Amazon Lex inserts the <code>AMAZON.FallbackIntent</code> and <code>AMAZON.KendraSearchIntent</code> intents in the list of possible intents for an utterance.</p>"""
    voice_settings: NotRequired["capo_lex_models_v2.types.voice_settings.VoiceSettings"]
    """<p>The Amazon Polly voice Amazon Lex uses for voice interaction with the user.</p>"""
    unified_speech_settings: NotRequired[
        "capo_lex_models_v2.types.unified_speech_settings.UnifiedSpeechSettings"
    ]
    """<p>The unified speech settings configured for the bot locale.</p>"""
    audio_filler_settings: NotRequired[
        "capo_lex_models_v2.types.audio_filler_settings.AudioFillerSettings"
    ]
    """<p>The audio filler settings configured for the bot locale.</p>"""
    speech_recognition_settings: NotRequired[
        "capo_lex_models_v2.types.speech_recognition_settings.SpeechRecognitionSettings"
    ]
    """<p>The speech-to-text settings configured for the bot locale.</p>"""
    intents_count: NotRequired["capo_lex_models_v2.types.resource_count.ResourceCount"]
    """<p>The number of intents defined for the locale.</p>"""
    slot_types_count: NotRequired[
        "capo_lex_models_v2.types.resource_count.ResourceCount"
    ]
    """<p>The number of slot types defined for the locale.</p>"""
    bot_locale_status: NotRequired[
        "capo_lex_models_v2.types.bot_locale_status.BotLocaleStatus"
    ]
    """<p>The status of the bot. If the status is <code>Failed</code>, the reasons for the failure are listed in the <code>failureReasons</code> field.</p>"""
    failure_reasons: NotRequired[
        "capo_lex_models_v2.types.failure_reasons.FailureReasons"
    ]
    """<p>if <code>botLocaleStatus</code> is <code>Failed</code>, Amazon Lex explains why it failed to build the bot.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the locale was created.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time that the locale was last updated.</p>"""
    last_build_submitted_date_time: NotRequired[
        "capo_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The date and time that the locale was last submitted for building.</p>"""
    bot_locale_history_events: NotRequired[
        "capo_lex_models_v2.types.bot_locale_history_events_list.BotLocaleHistoryEventsList"
    ]
    """<p>History of changes, such as when a locale is used in an alias, that have taken place for the locale.</p>"""
    recommended_actions: NotRequired[
        "capo_lex_models_v2.types.recommended_actions.RecommendedActions"
    ]
    """<p>Recommended actions to take to resolve an error in the <code>failureReasons</code> field.</p>"""
    generative_ai_settings: NotRequired[
        "capo_lex_models_v2.types.generative_ai_settings.GenerativeAISettings"
    ]
    """<p>Contains settings for Amazon Bedrock's generative AI features for your bot locale.</p>"""
    speech_detection_sensitivity: NotRequired[
        "capo_lex_models_v2.types.speech_detection_sensitivity.SpeechDetectionSensitivity"
    ]
    """<p>The sensitivity level for voice activity detection (VAD) configured for the bot locale.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeBotLocaleResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "locale_name" in value:
        out["localeName"] = value["locale_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "nlu_intent_confidence_threshold" in value:
        out["nluIntentConfidenceThreshold"] = value["nlu_intent_confidence_threshold"]
    if "voice_settings" in value:
        import capo_lex_models_v2.types.voice_settings

        out["voiceSettings"] = capo_lex_models_v2.types.voice_settings.serialize_json(
            value["voice_settings"]
        )
    if "unified_speech_settings" in value:
        import capo_lex_models_v2.types.unified_speech_settings

        out["unifiedSpeechSettings"] = (
            capo_lex_models_v2.types.unified_speech_settings.serialize_json(
                value["unified_speech_settings"]
            )
        )
    if "audio_filler_settings" in value:
        import capo_lex_models_v2.types.audio_filler_settings

        out["audioFillerSettings"] = (
            capo_lex_models_v2.types.audio_filler_settings.serialize_json(
                value["audio_filler_settings"]
            )
        )
    if "speech_recognition_settings" in value:
        import capo_lex_models_v2.types.speech_recognition_settings

        out["speechRecognitionSettings"] = (
            capo_lex_models_v2.types.speech_recognition_settings.serialize_json(
                value["speech_recognition_settings"]
            )
        )
    if "intents_count" in value:
        out["intentsCount"] = value["intents_count"]
    if "slot_types_count" in value:
        out["slotTypesCount"] = value["slot_types_count"]
    if "bot_locale_status" in value:
        import capo_lex_models_v2.types.bot_locale_status

        out["botLocaleStatus"] = (
            capo_lex_models_v2.types.bot_locale_status.serialize_json(
                value["bot_locale_status"]
            )
        )
    if "failure_reasons" in value:
        import capo_lex_models_v2.types.failure_reasons

        out["failureReasons"] = capo_lex_models_v2.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["last_updated_date_time"]
        )
    if "last_build_submitted_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastBuildSubmittedDateTime"] = (
            capo_lex_models_v2.types.timestamp.serialize_json(
                value["last_build_submitted_date_time"]
            )
        )
    if "bot_locale_history_events" in value:
        import capo_lex_models_v2.types.bot_locale_history_events_list

        out["botLocaleHistoryEvents"] = (
            capo_lex_models_v2.types.bot_locale_history_events_list.serialize_json(
                value["bot_locale_history_events"]
            )
        )
    if "recommended_actions" in value:
        import capo_lex_models_v2.types.recommended_actions

        out["recommendedActions"] = (
            capo_lex_models_v2.types.recommended_actions.serialize_json(
                value["recommended_actions"]
            )
        )
    if "generative_ai_settings" in value:
        import capo_lex_models_v2.types.generative_ai_settings

        out["generativeAISettings"] = (
            capo_lex_models_v2.types.generative_ai_settings.serialize_json(
                value["generative_ai_settings"]
            )
        )
    if "speech_detection_sensitivity" in value:
        import capo_lex_models_v2.types.speech_detection_sensitivity

        out["speechDetectionSensitivity"] = (
            capo_lex_models_v2.types.speech_detection_sensitivity.serialize_json(
                value["speech_detection_sensitivity"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeBotLocaleResponse:
    out: DescribeBotLocaleResponse = {}  # type: ignore[typeddict-item]
    if "botId" in data:
        out["bot_id"] = data["botId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "localeName" in data:
        out["locale_name"] = data["localeName"]
    if "description" in data:
        out["description"] = data["description"]
    if "nluIntentConfidenceThreshold" in data:
        out["nlu_intent_confidence_threshold"] = data["nluIntentConfidenceThreshold"]
    if "voiceSettings" in data:
        import capo_lex_models_v2.types.voice_settings

        out["voice_settings"] = (
            capo_lex_models_v2.types.voice_settings.deserialize_json(
                data["voiceSettings"]
            )
        )
    if "unifiedSpeechSettings" in data:
        import capo_lex_models_v2.types.unified_speech_settings

        out["unified_speech_settings"] = (
            capo_lex_models_v2.types.unified_speech_settings.deserialize_json(
                data["unifiedSpeechSettings"]
            )
        )
    if "audioFillerSettings" in data:
        import capo_lex_models_v2.types.audio_filler_settings

        out["audio_filler_settings"] = (
            capo_lex_models_v2.types.audio_filler_settings.deserialize_json(
                data["audioFillerSettings"]
            )
        )
    if "speechRecognitionSettings" in data:
        import capo_lex_models_v2.types.speech_recognition_settings

        out["speech_recognition_settings"] = (
            capo_lex_models_v2.types.speech_recognition_settings.deserialize_json(
                data["speechRecognitionSettings"]
            )
        )
    if "intentsCount" in data:
        out["intents_count"] = data["intentsCount"]
    if "slotTypesCount" in data:
        out["slot_types_count"] = data["slotTypesCount"]
    if "botLocaleStatus" in data:
        import capo_lex_models_v2.types.bot_locale_status

        out["bot_locale_status"] = (
            capo_lex_models_v2.types.bot_locale_status.deserialize_json(
                data["botLocaleStatus"]
            )
        )
    if "failureReasons" in data:
        import capo_lex_models_v2.types.failure_reasons

        out["failure_reasons"] = (
            capo_lex_models_v2.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    if "creationDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if "lastUpdatedDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    if "lastBuildSubmittedDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["last_build_submitted_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["lastBuildSubmittedDateTime"]
            )
        )
    if "botLocaleHistoryEvents" in data:
        import capo_lex_models_v2.types.bot_locale_history_events_list

        out["bot_locale_history_events"] = (
            capo_lex_models_v2.types.bot_locale_history_events_list.deserialize_json(
                data["botLocaleHistoryEvents"]
            )
        )
    if "recommendedActions" in data:
        import capo_lex_models_v2.types.recommended_actions

        out["recommended_actions"] = (
            capo_lex_models_v2.types.recommended_actions.deserialize_json(
                data["recommendedActions"]
            )
        )
    if "generativeAISettings" in data:
        import capo_lex_models_v2.types.generative_ai_settings

        out["generative_ai_settings"] = (
            capo_lex_models_v2.types.generative_ai_settings.deserialize_json(
                data["generativeAISettings"]
            )
        )
    if "speechDetectionSensitivity" in data:
        import capo_lex_models_v2.types.speech_detection_sensitivity

        out["speech_detection_sensitivity"] = (
            capo_lex_models_v2.types.speech_detection_sensitivity.deserialize_json(
                data["speechDetectionSensitivity"]
            )
        )
    return out
