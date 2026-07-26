"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AudioFillerSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.audio_filler_delay_in_milliseconds
    import capo_lex_models_v2.types.audio_filler_delivery_delay_in_milliseconds
    import capo_lex_models_v2.types.audio_filler_duration_in_milliseconds
    import capo_lex_models_v2.types.audio_filler_type
    import capo_lex_models_v2.types.boolean


class AudioFillerSettings(TypedDict, closed=True):
    enabled: "capo_lex_models_v2.types.boolean.Boolean"
    """<p>Specifies whether audio filler playback is enabled for the bot locale. Set to <code>true</code> to play filler audio while Amazon Lex processes a user utterance. Set to <code>false</code> to disable filler audio.</p>"""
    audio_type: NotRequired[
        "capo_lex_models_v2.types.audio_filler_type.AudioFillerType"
    ]
    """<p>The identifier of the audio filler to play while Amazon Lex processes the user's input. This field is required when <code>enabled</code> is <code>true</code>.</p>"""
    start_delay_in_milliseconds: NotRequired[
        "capo_lex_models_v2.types.audio_filler_delay_in_milliseconds.AudioFillerDelayInMilliseconds"
    ]
    """<p>The time, in milliseconds, to wait after the end of the user's utterance before starting audio filler playback. Valid range is <code>500</code> to <code>5000</code> milliseconds. If not specified, Amazon Lex uses a default of <code>2500</code> milliseconds.</p>"""
    minimum_play_duration_in_milliseconds: NotRequired[
        "capo_lex_models_v2.types.audio_filler_duration_in_milliseconds.AudioFillerDurationInMilliseconds"
    ]
    """<p>The minimum time, in milliseconds, that audio filler plays once it has started, even if the bot response becomes ready sooner. Valid range is <code>1000</code> to <code>5000</code> milliseconds. If not specified, Amazon Lex uses a default of <code>3000</code> milliseconds.</p>"""
    response_delivery_delay_in_milliseconds: NotRequired[
        "capo_lex_models_v2.types.audio_filler_delivery_delay_in_milliseconds.AudioFillerDeliveryDelayInMilliseconds"
    ]
    """<p>The silent delay, in milliseconds, inserted between the end of audio filler playback and the start of the bot's response. Valid range is <code>200</code> to <code>1000</code> milliseconds. If not specified, Amazon Lex uses a default of <code>500</code> milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioFillerSettings) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "audio_type" in value:
        import capo_lex_models_v2.types.audio_filler_type

        out["audioType"] = capo_lex_models_v2.types.audio_filler_type.serialize_json(
            value["audio_type"]
        )
    if "start_delay_in_milliseconds" in value:
        out["startDelayInMilliseconds"] = value["start_delay_in_milliseconds"]
    if "minimum_play_duration_in_milliseconds" in value:
        out["minimumPlayDurationInMilliseconds"] = value[
            "minimum_play_duration_in_milliseconds"
        ]
    if "response_delivery_delay_in_milliseconds" in value:
        out["responseDeliveryDelayInMilliseconds"] = value[
            "response_delivery_delay_in_milliseconds"
        ]
    return out


def deserialize_json(data: dict) -> AudioFillerSettings:
    out: AudioFillerSettings = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "audioType" in data:
        import capo_lex_models_v2.types.audio_filler_type

        out["audio_type"] = capo_lex_models_v2.types.audio_filler_type.deserialize_json(
            data["audioType"]
        )
    if "startDelayInMilliseconds" in data:
        out["start_delay_in_milliseconds"] = data["startDelayInMilliseconds"]
    if "minimumPlayDurationInMilliseconds" in data:
        out["minimum_play_duration_in_milliseconds"] = data[
            "minimumPlayDurationInMilliseconds"
        ]
    if "responseDeliveryDelayInMilliseconds" in data:
        out["response_delivery_delay_in_milliseconds"] = data[
            "responseDeliveryDelayInMilliseconds"
        ]
    return out
