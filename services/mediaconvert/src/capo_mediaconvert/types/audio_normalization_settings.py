"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioNormalizationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__double_min_negative8_max0
    import capo_mediaconvert.types.__double_min_negative59_max0
    import capo_mediaconvert.types.__integer_min_negative70_max0
    import capo_mediaconvert.types.audio_normalization_algorithm
    import capo_mediaconvert.types.audio_normalization_algorithm_control
    import capo_mediaconvert.types.audio_normalization_loudness_logging
    import capo_mediaconvert.types.audio_normalization_peak_calculation


class AudioNormalizationSettings(TypedDict, closed=True):
    algorithm: NotRequired[
        "capo_mediaconvert.types.audio_normalization_algorithm.AudioNormalizationAlgorithm"
    ]
    """Choose one of the following audio normalization algorithms: ITU-R BS.1770-1: Ungated loudness. A measurement of ungated average loudness for an entire piece of content, suitable for measurement of short-form content under ATSC recommendation A/85. Supports up to 5.1 audio channels. ITU-R BS.1770-2: Gated loudness. A measurement of gated average loudness compliant with the requirements of EBU-R128. Supports up to 5.1 audio channels. ITU-R BS.1770-3: Modified peak. The same loudness measurement algorithm as 1770-2, with an updated true peak measurement. ITU-R BS.1770-4: Higher channel count. Allows for more audio channels than the other algorithms, including configurations such as 7.1."""
    algorithm_control: NotRequired[
        "capo_mediaconvert.types.audio_normalization_algorithm_control.AudioNormalizationAlgorithmControl"
    ]
    """When enabled the output audio is corrected using the chosen algorithm. If disabled, the audio will be measured but not adjusted."""
    correction_gate_level: NotRequired[
        "capo_mediaconvert.types.__integer_min_negative70_max0.__integerMinNegative70Max0"
    ]
    """Content measuring above this level will be corrected to the target level. Content measuring below this level will not be corrected."""
    loudness_logging: NotRequired[
        "capo_mediaconvert.types.audio_normalization_loudness_logging.AudioNormalizationLoudnessLogging"
    ]
    """If set to LOG, log each output's audio track loudness to a CSV file."""
    peak_calculation: NotRequired[
        "capo_mediaconvert.types.audio_normalization_peak_calculation.AudioNormalizationPeakCalculation"
    ]
    """If set to TRUE_PEAK, calculate and log the TruePeak for each output's audio track loudness."""
    target_lkfs: NotRequired[
        "capo_mediaconvert.types.__double_min_negative59_max0.__doubleMinNegative59Max0"
    ]
    """When you use Audio normalization, optionally use this setting to specify a target loudness. If you don't specify a value here, the encoder chooses a value for you, based on the algorithm that you choose for Algorithm. If you choose algorithm 1770-1, the encoder will choose -24 LKFS; otherwise, the encoder will choose -23 LKFS."""
    true_peak_limiter_threshold: NotRequired[
        "capo_mediaconvert.types.__double_min_negative8_max0.__doubleMinNegative8Max0"
    ]
    """Specify the True-peak limiter threshold in decibels relative to full scale (dBFS). The peak inter-audio sample loudness in your output will be limited to the value that you specify, without affecting the overall target LKFS. Enter a value from 0 to -8. Leave blank to use the default value 0."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioNormalizationSettings) -> dict:
    out: dict = {}
    if "algorithm" in value:
        import capo_mediaconvert.types.audio_normalization_algorithm

        out["algorithm"] = (
            capo_mediaconvert.types.audio_normalization_algorithm.serialize_json(
                value["algorithm"]
            )
        )
    if "algorithm_control" in value:
        import capo_mediaconvert.types.audio_normalization_algorithm_control

        out["algorithmControl"] = (
            capo_mediaconvert.types.audio_normalization_algorithm_control.serialize_json(
                value["algorithm_control"]
            )
        )
    if "correction_gate_level" in value:
        out["correctionGateLevel"] = value["correction_gate_level"]
    if "loudness_logging" in value:
        import capo_mediaconvert.types.audio_normalization_loudness_logging

        out["loudnessLogging"] = (
            capo_mediaconvert.types.audio_normalization_loudness_logging.serialize_json(
                value["loudness_logging"]
            )
        )
    if "peak_calculation" in value:
        import capo_mediaconvert.types.audio_normalization_peak_calculation

        out["peakCalculation"] = (
            capo_mediaconvert.types.audio_normalization_peak_calculation.serialize_json(
                value["peak_calculation"]
            )
        )
    if "target_lkfs" in value:
        out["targetLkfs"] = value["target_lkfs"]
    if "true_peak_limiter_threshold" in value:
        out["truePeakLimiterThreshold"] = value["true_peak_limiter_threshold"]
    return out


def deserialize_json(data: dict) -> AudioNormalizationSettings:
    out: AudioNormalizationSettings = {}  # type: ignore[typeddict-item]
    if "algorithm" in data:
        import capo_mediaconvert.types.audio_normalization_algorithm

        out["algorithm"] = (
            capo_mediaconvert.types.audio_normalization_algorithm.deserialize_json(
                data["algorithm"]
            )
        )
    if "algorithmControl" in data:
        import capo_mediaconvert.types.audio_normalization_algorithm_control

        out["algorithm_control"] = (
            capo_mediaconvert.types.audio_normalization_algorithm_control.deserialize_json(
                data["algorithmControl"]
            )
        )
    if "correctionGateLevel" in data:
        out["correction_gate_level"] = data["correctionGateLevel"]
    if "loudnessLogging" in data:
        import capo_mediaconvert.types.audio_normalization_loudness_logging

        out["loudness_logging"] = (
            capo_mediaconvert.types.audio_normalization_loudness_logging.deserialize_json(
                data["loudnessLogging"]
            )
        )
    if "peakCalculation" in data:
        import capo_mediaconvert.types.audio_normalization_peak_calculation

        out["peak_calculation"] = (
            capo_mediaconvert.types.audio_normalization_peak_calculation.deserialize_json(
                data["peakCalculation"]
            )
        )
    if "targetLkfs" in data:
        out["target_lkfs"] = data["targetLkfs"]
    if "truePeakLimiterThreshold" in data:
        out["true_peak_limiter_threshold"] = data["truePeakLimiterThreshold"]
    return out
