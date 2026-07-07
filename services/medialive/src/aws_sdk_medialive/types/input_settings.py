"""Generated from Smithy shape ``com.amazonaws.medialive#InputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min1_max5
    import aws_sdk_medialive.types.__integer_min32_max8191
    import aws_sdk_medialive.types.__list_of_audio_selector
    import aws_sdk_medialive.types.__list_of_caption_selector
    import aws_sdk_medialive.types.input_deblock_filter
    import aws_sdk_medialive.types.input_denoise_filter
    import aws_sdk_medialive.types.input_filter
    import aws_sdk_medialive.types.input_source_end_behavior
    import aws_sdk_medialive.types.network_input_settings
    import aws_sdk_medialive.types.smpte2038_data_preference
    import aws_sdk_medialive.types.video_selector


class InputSettings(TypedDict, closed=True):
    audio_selectors: NotRequired[
        "aws_sdk_medialive.types.__list_of_audio_selector.__listOfAudioSelector"
    ]
    """Used to select the audio stream to decode for inputs that have multiple available."""
    caption_selectors: NotRequired[
        "aws_sdk_medialive.types.__list_of_caption_selector.__listOfCaptionSelector"
    ]
    """Used to select the caption input to use for inputs that have multiple available."""
    deblock_filter: NotRequired[
        "aws_sdk_medialive.types.input_deblock_filter.InputDeblockFilter"
    ]
    """Enable or disable the deblock filter when filtering."""
    denoise_filter: NotRequired[
        "aws_sdk_medialive.types.input_denoise_filter.InputDenoiseFilter"
    ]
    """Enable or disable the denoise filter when filtering."""
    filter_strength: NotRequired[
        "aws_sdk_medialive.types.__integer_min1_max5.__integerMin1Max5"
    ]
    """Adjusts the magnitude of filtering from 1 (minimal) to 5 (strongest)."""
    input_filter: NotRequired["aws_sdk_medialive.types.input_filter.InputFilter"]
    """Turns on the filter for this input. MPEG-2 inputs have the deblocking filter enabled by default. 1) auto - filtering will be applied depending on input type/quality 2) disabled - no filtering will be applied to the input 3) forced - filtering will be applied regardless of input type"""
    network_input_settings: NotRequired[
        "aws_sdk_medialive.types.network_input_settings.NetworkInputSettings"
    ]
    """Input settings."""
    scte35_pid: NotRequired[
        "aws_sdk_medialive.types.__integer_min32_max8191.__integerMin32Max8191"
    ]
    """PID from which to read SCTE-35 messages. If left undefined, EML will select the first SCTE-35 PID found in the input."""
    smpte2038_data_preference: NotRequired[
        "aws_sdk_medialive.types.smpte2038_data_preference.Smpte2038DataPreference"
    ]
    """Specifies whether to extract applicable ancillary data from a SMPTE-2038 source in this input. Applicable data types are captions, timecode, AFD, and SCTE-104 messages. - PREFER: Extract from SMPTE-2038 if present in this input, otherwise extract from another source (if any). - IGNORE: Never extract any ancillary data from SMPTE-2038."""
    source_end_behavior: NotRequired[
        "aws_sdk_medialive.types.input_source_end_behavior.InputSourceEndBehavior"
    ]
    """Loop input if it is a file. This allows a file input to be streamed indefinitely."""
    video_selector: NotRequired["aws_sdk_medialive.types.video_selector.VideoSelector"]
    """Informs which video elementary stream to decode for input types that have multiple available."""


# --- restJson1 ser/de ---
def serialize_json(value: InputSettings) -> dict:
    out: dict = {}
    if "audio_selectors" in value:
        import aws_sdk_medialive.types.__list_of_audio_selector

        out["audioSelectors"] = (
            aws_sdk_medialive.types.__list_of_audio_selector.serialize_json(
                value["audio_selectors"]
            )
        )
    if "caption_selectors" in value:
        import aws_sdk_medialive.types.__list_of_caption_selector

        out["captionSelectors"] = (
            aws_sdk_medialive.types.__list_of_caption_selector.serialize_json(
                value["caption_selectors"]
            )
        )
    if "deblock_filter" in value:
        import aws_sdk_medialive.types.input_deblock_filter

        out["deblockFilter"] = (
            aws_sdk_medialive.types.input_deblock_filter.serialize_json(
                value["deblock_filter"]
            )
        )
    if "denoise_filter" in value:
        import aws_sdk_medialive.types.input_denoise_filter

        out["denoiseFilter"] = (
            aws_sdk_medialive.types.input_denoise_filter.serialize_json(
                value["denoise_filter"]
            )
        )
    if "filter_strength" in value:
        out["filterStrength"] = value["filter_strength"]
    if "input_filter" in value:
        import aws_sdk_medialive.types.input_filter

        out["inputFilter"] = aws_sdk_medialive.types.input_filter.serialize_json(
            value["input_filter"]
        )
    if "network_input_settings" in value:
        import aws_sdk_medialive.types.network_input_settings

        out["networkInputSettings"] = (
            aws_sdk_medialive.types.network_input_settings.serialize_json(
                value["network_input_settings"]
            )
        )
    if "scte35_pid" in value:
        out["scte35Pid"] = value["scte35_pid"]
    if "smpte2038_data_preference" in value:
        import aws_sdk_medialive.types.smpte2038_data_preference

        out["smpte2038DataPreference"] = (
            aws_sdk_medialive.types.smpte2038_data_preference.serialize_json(
                value["smpte2038_data_preference"]
            )
        )
    if "source_end_behavior" in value:
        import aws_sdk_medialive.types.input_source_end_behavior

        out["sourceEndBehavior"] = (
            aws_sdk_medialive.types.input_source_end_behavior.serialize_json(
                value["source_end_behavior"]
            )
        )
    if "video_selector" in value:
        import aws_sdk_medialive.types.video_selector

        out["videoSelector"] = aws_sdk_medialive.types.video_selector.serialize_json(
            value["video_selector"]
        )
    return out


def deserialize_json(data: dict) -> InputSettings:
    out: InputSettings = {}  # type: ignore[typeddict-item]
    if "audioSelectors" in data:
        import aws_sdk_medialive.types.__list_of_audio_selector

        out["audio_selectors"] = (
            aws_sdk_medialive.types.__list_of_audio_selector.deserialize_json(
                data["audioSelectors"]
            )
        )
    if "captionSelectors" in data:
        import aws_sdk_medialive.types.__list_of_caption_selector

        out["caption_selectors"] = (
            aws_sdk_medialive.types.__list_of_caption_selector.deserialize_json(
                data["captionSelectors"]
            )
        )
    if "deblockFilter" in data:
        import aws_sdk_medialive.types.input_deblock_filter

        out["deblock_filter"] = (
            aws_sdk_medialive.types.input_deblock_filter.deserialize_json(
                data["deblockFilter"]
            )
        )
    if "denoiseFilter" in data:
        import aws_sdk_medialive.types.input_denoise_filter

        out["denoise_filter"] = (
            aws_sdk_medialive.types.input_denoise_filter.deserialize_json(
                data["denoiseFilter"]
            )
        )
    if "filterStrength" in data:
        out["filter_strength"] = data["filterStrength"]
    if "inputFilter" in data:
        import aws_sdk_medialive.types.input_filter

        out["input_filter"] = aws_sdk_medialive.types.input_filter.deserialize_json(
            data["inputFilter"]
        )
    if "networkInputSettings" in data:
        import aws_sdk_medialive.types.network_input_settings

        out["network_input_settings"] = (
            aws_sdk_medialive.types.network_input_settings.deserialize_json(
                data["networkInputSettings"]
            )
        )
    if "scte35Pid" in data:
        out["scte35_pid"] = data["scte35Pid"]
    if "smpte2038DataPreference" in data:
        import aws_sdk_medialive.types.smpte2038_data_preference

        out["smpte2038_data_preference"] = (
            aws_sdk_medialive.types.smpte2038_data_preference.deserialize_json(
                data["smpte2038DataPreference"]
            )
        )
    if "sourceEndBehavior" in data:
        import aws_sdk_medialive.types.input_source_end_behavior

        out["source_end_behavior"] = (
            aws_sdk_medialive.types.input_source_end_behavior.deserialize_json(
                data["sourceEndBehavior"]
            )
        )
    if "videoSelector" in data:
        import aws_sdk_medialive.types.video_selector

        out["video_selector"] = aws_sdk_medialive.types.video_selector.deserialize_json(
            data["videoSelector"]
        )
    return out
