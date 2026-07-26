"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SessionSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.analytics_channel
    import capo_lex_models_v2.types.analytics_long_value
    import capo_lex_models_v2.types.analytics_modality
    import capo_lex_models_v2.types.analytics_originating_request_id
    import capo_lex_models_v2.types.analytics_session_id
    import capo_lex_models_v2.types.bot_alias_id
    import capo_lex_models_v2.types.conversation_end_state
    import capo_lex_models_v2.types.invoked_intent_samples
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.numerical_bot_version
    import capo_lex_models_v2.types.timestamp


class SessionSpecification(TypedDict, closed=True):
    bot_alias_id: NotRequired["capo_lex_models_v2.types.bot_alias_id.BotAliasId"]
    """<p>The identifier of the alias of the bot that the session was held with.</p>"""
    bot_version: NotRequired[
        "capo_lex_models_v2.types.numerical_bot_version.NumericalBotVersion"
    ]
    """<p>The version of the bot that the session was held with.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The locale of the bot that the session was held with.</p>"""
    channel: NotRequired["capo_lex_models_v2.types.analytics_channel.AnalyticsChannel"]
    """<p>The channel that is integrated with the bot that the session was held with.</p>"""
    session_id: NotRequired[
        "capo_lex_models_v2.types.analytics_session_id.AnalyticsSessionId"
    ]
    """<p>The identifier of the session.</p>"""
    conversation_start_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time when the conversation began. A conversation is defined as a unique combination of a <code>sessionId</code> and an <code>originatingRequestId</code>.</p>"""
    conversation_end_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time when the conversation ended. A conversation is defined as a unique combination of a <code>sessionId</code> and an <code>originatingRequestId</code>.</p>"""
    conversation_duration_seconds: NotRequired[
        "capo_lex_models_v2.types.analytics_long_value.AnalyticsLongValue"
    ]
    """<p>The duration of the conversation in seconds. A conversation is defined as a unique combination of a <code>sessionId</code> and an <code>originatingRequestId</code>.</p>"""
    conversation_end_state: NotRequired[
        "capo_lex_models_v2.types.conversation_end_state.ConversationEndState"
    ]
    """<p>The final state of the conversation. A conversation is defined as a unique combination of a <code>sessionId</code> and an <code>originatingRequestId</code>.</p>"""
    mode: NotRequired["capo_lex_models_v2.types.analytics_modality.AnalyticsModality"]
    """<p>The mode of the session. The possible values are as follows:</p> <ul> <li> <p> <code>Speech</code> – The session was spoken.</p> </li> <li> <p> <code>Text</code> – The session was written.</p> </li> <li> <p> <code>DTMF</code> – The session used a touch-tone keypad (Dual Tone Multi-Frequency).</p> </li> <li> <p> <code>MultiMode</code> – The session used multiple modes.</p> </li> </ul>"""
    number_of_turns: NotRequired[
        "capo_lex_models_v2.types.analytics_long_value.AnalyticsLongValue"
    ]
    """<p>The number of turns that the session took.</p>"""
    invoked_intent_samples: NotRequired[
        "capo_lex_models_v2.types.invoked_intent_samples.InvokedIntentSamples"
    ]
    """<p>A list of objects containing the name of an intent that was invoked.</p>"""
    originating_request_id: NotRequired[
        "capo_lex_models_v2.types.analytics_originating_request_id.AnalyticsOriginatingRequestId"
    ]
    """<p>The identifier of the first request in a session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionSpecification) -> dict:
    out: dict = {}
    if "bot_alias_id" in value:
        out["botAliasId"] = value["bot_alias_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "channel" in value:
        out["channel"] = value["channel"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "conversation_start_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["conversationStartTime"] = (
            capo_lex_models_v2.types.timestamp.serialize_json(
                value["conversation_start_time"]
            )
        )
    if "conversation_end_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["conversationEndTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["conversation_end_time"]
        )
    if "conversation_duration_seconds" in value:
        out["conversationDurationSeconds"] = value["conversation_duration_seconds"]
    if "conversation_end_state" in value:
        import capo_lex_models_v2.types.conversation_end_state

        out["conversationEndState"] = (
            capo_lex_models_v2.types.conversation_end_state.serialize_json(
                value["conversation_end_state"]
            )
        )
    if "mode" in value:
        import capo_lex_models_v2.types.analytics_modality

        out["mode"] = capo_lex_models_v2.types.analytics_modality.serialize_json(
            value["mode"]
        )
    if "number_of_turns" in value:
        out["numberOfTurns"] = value["number_of_turns"]
    if "invoked_intent_samples" in value:
        import capo_lex_models_v2.types.invoked_intent_samples

        out["invokedIntentSamples"] = (
            capo_lex_models_v2.types.invoked_intent_samples.serialize_json(
                value["invoked_intent_samples"]
            )
        )
    if "originating_request_id" in value:
        out["originatingRequestId"] = value["originating_request_id"]
    return out


def deserialize_json(data: dict) -> SessionSpecification:
    out: SessionSpecification = {}  # type: ignore[typeddict-item]
    if "botAliasId" in data:
        out["bot_alias_id"] = data["botAliasId"]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "localeId" in data:
        out["locale_id"] = data["localeId"]
    if "channel" in data:
        out["channel"] = data["channel"]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "conversationStartTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["conversation_start_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["conversationStartTime"]
            )
        )
    if "conversationEndTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["conversation_end_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["conversationEndTime"]
            )
        )
    if "conversationDurationSeconds" in data:
        out["conversation_duration_seconds"] = data["conversationDurationSeconds"]
    if "conversationEndState" in data:
        import capo_lex_models_v2.types.conversation_end_state

        out["conversation_end_state"] = (
            capo_lex_models_v2.types.conversation_end_state.deserialize_json(
                data["conversationEndState"]
            )
        )
    if "mode" in data:
        import capo_lex_models_v2.types.analytics_modality

        out["mode"] = capo_lex_models_v2.types.analytics_modality.deserialize_json(
            data["mode"]
        )
    if "numberOfTurns" in data:
        out["number_of_turns"] = data["numberOfTurns"]
    if "invokedIntentSamples" in data:
        import capo_lex_models_v2.types.invoked_intent_samples

        out["invoked_intent_samples"] = (
            capo_lex_models_v2.types.invoked_intent_samples.deserialize_json(
                data["invokedIntentSamples"]
            )
        )
    if "originatingRequestId" in data:
        out["originating_request_id"] = data["originatingRequestId"]
    return out
