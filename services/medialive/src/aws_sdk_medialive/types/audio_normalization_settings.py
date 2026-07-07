"""Generated from Smithy shape ``com.amazonaws.medialive#AudioNormalizationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__double_min_negative8_max0
    import aws_sdk_medialive.types.__double_min_negative59_max0
    import aws_sdk_medialive.types.audio_normalization_algorithm
    import aws_sdk_medialive.types.audio_normalization_algorithm_control
    import aws_sdk_medialive.types.audio_normalization_peak_calculation


class AudioNormalizationSettings(TypedDict, closed=True):
    algorithm: NotRequired[
        "aws_sdk_medialive.types.audio_normalization_algorithm.AudioNormalizationAlgorithm"
    ]
    """Choose one of the following audio normalization algorithms: ITU-R BS.1770-1: Ungated loudness. A measurement of ungated average loudness for an entire piece of content, suitable for measurement of short-form content under ATSC recommendation A/85. Supports up to 5.1 audio channels. ITU-R BS.1770-2: Gated loudness. A measurement of gated average loudness compliant with the requirements of EBU-R128. Supports up to 5.1 audio channels. ITU-R BS.1770-3: Modified peak. The same loudness measurement algorithm as 1770-2, with an updated true peak measurement. ITU-R BS.1770-4: Higher channel count. Allows for more audio channels than the other algorithms, including configurations such as 7.1."""
    algorithm_control: NotRequired[
        "aws_sdk_medialive.types.audio_normalization_algorithm_control.AudioNormalizationAlgorithmControl"
    ]
    """When set to correctAudio the output audio is corrected using the chosen algorithm. If set to measureOnly, the audio will be measured but not adjusted."""
    target_lkfs: NotRequired[
        "aws_sdk_medialive.types.__double_min_negative59_max0.__doubleMinNegative59Max0"
    ]
    """Target LKFS(loudness) to adjust volume to. If no value is entered, a default value will be used according to the chosen algorithm. The CALM Act recommends a target of -24 LKFS. The EBU R-128 specification recommends a target of -23 LKFS."""
    peak_calculation: NotRequired[
        "aws_sdk_medialive.types.audio_normalization_peak_calculation.AudioNormalizationPeakCalculation"
    ]
    """If set to TRUE_PEAK, calculate the TruePeak for each output's audio track loudness."""
    peak_limiter_threshold: NotRequired[
        "aws_sdk_medialive.types.__double_min_negative8_max0.__doubleMinNegative8Max0"
    ]
    """Peak limiter threshold in decibels relative to true peak (dBTP) if TRUE_PEAK is enabled. If TRUE_PEAK is not enabled a full scale (dbFS) value is used. The peak inter-audio sample loudness in your output will be limited to the value that you specify, without affecting the overall target LKFS. Leave blank to use the default value 0."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioNormalizationSettings) -> dict:
    out: dict = {}
    if "algorithm" in value:
        import aws_sdk_medialive.types.audio_normalization_algorithm

        out["algorithm"] = (
            aws_sdk_medialive.types.audio_normalization_algorithm.serialize_json(
                value["algorithm"]
            )
        )
    if "algorithm_control" in value:
        import aws_sdk_medialive.types.audio_normalization_algorithm_control

        out["algorithmControl"] = (
            aws_sdk_medialive.types.audio_normalization_algorithm_control.serialize_json(
                value["algorithm_control"]
            )
        )
    if "target_lkfs" in value:
        out["targetLkfs"] = value["target_lkfs"]
    if "peak_calculation" in value:
        import aws_sdk_medialive.types.audio_normalization_peak_calculation

        out["peakCalculation"] = (
            aws_sdk_medialive.types.audio_normalization_peak_calculation.serialize_json(
                value["peak_calculation"]
            )
        )
    if "peak_limiter_threshold" in value:
        out["peakLimiterThreshold"] = value["peak_limiter_threshold"]
    return out


def deserialize_json(data: dict) -> AudioNormalizationSettings:
    out: AudioNormalizationSettings = {}  # type: ignore[typeddict-item]
    if "algorithm" in data:
        import aws_sdk_medialive.types.audio_normalization_algorithm

        out["algorithm"] = (
            aws_sdk_medialive.types.audio_normalization_algorithm.deserialize_json(
                data["algorithm"]
            )
        )
    if "algorithmControl" in data:
        import aws_sdk_medialive.types.audio_normalization_algorithm_control

        out["algorithm_control"] = (
            aws_sdk_medialive.types.audio_normalization_algorithm_control.deserialize_json(
                data["algorithmControl"]
            )
        )
    if "targetLkfs" in data:
        out["target_lkfs"] = data["targetLkfs"]
    if "peakCalculation" in data:
        import aws_sdk_medialive.types.audio_normalization_peak_calculation

        out["peak_calculation"] = (
            aws_sdk_medialive.types.audio_normalization_peak_calculation.deserialize_json(
                data["peakCalculation"]
            )
        )
    if "peakLimiterThreshold" in data:
        out["peak_limiter_threshold"] = data["peakLimiterThreshold"]
    return out
