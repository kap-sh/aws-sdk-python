"""Generated from Smithy shape ``com.amazonaws.groundstation#AntennaDownlinkDemodDecodeConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.decode_config
    import aws_sdk_groundstation.types.demodulation_config
    import aws_sdk_groundstation.types.spectrum_config


class AntennaDownlinkDemodDecodeConfig(TypedDict):
    spectrum_config: "aws_sdk_groundstation.types.spectrum_config.SpectrumConfig"
    """<p>Information about the spectral <code>Config</code>.</p>"""
    demodulation_config: (
        "aws_sdk_groundstation.types.demodulation_config.DemodulationConfig"
    )
    """<p>Information about the demodulation <code>Config</code>.</p>"""
    decode_config: "aws_sdk_groundstation.types.decode_config.DecodeConfig"
    """<p>Information about the decode <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AntennaDownlinkDemodDecodeConfig) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.spectrum_config

    out["spectrumConfig"] = aws_sdk_groundstation.types.spectrum_config.serialize_json(
        value["spectrum_config"]
    )
    import aws_sdk_groundstation.types.demodulation_config

    out["demodulationConfig"] = (
        aws_sdk_groundstation.types.demodulation_config.serialize_json(
            value["demodulation_config"]
        )
    )
    import aws_sdk_groundstation.types.decode_config

    out["decodeConfig"] = aws_sdk_groundstation.types.decode_config.serialize_json(
        value["decode_config"]
    )
    return out


def deserialize_json(data: dict) -> AntennaDownlinkDemodDecodeConfig:
    out: AntennaDownlinkDemodDecodeConfig = {}  # type: ignore[typeddict-item]
    if "spectrumConfig" in data:
        import aws_sdk_groundstation.types.spectrum_config

        out["spectrum_config"] = (
            aws_sdk_groundstation.types.spectrum_config.deserialize_json(
                data["spectrumConfig"]
            )
        )
    else:
        raise DeserializationError(
            "AntennaDownlinkDemodDecodeConfig.spectrum_config required"
        )
    if "demodulationConfig" in data:
        import aws_sdk_groundstation.types.demodulation_config

        out["demodulation_config"] = (
            aws_sdk_groundstation.types.demodulation_config.deserialize_json(
                data["demodulationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "AntennaDownlinkDemodDecodeConfig.demodulation_config required"
        )
    if "decodeConfig" in data:
        import aws_sdk_groundstation.types.decode_config

        out["decode_config"] = (
            aws_sdk_groundstation.types.decode_config.deserialize_json(
                data["decodeConfig"]
            )
        )
    else:
        raise DeserializationError(
            "AntennaDownlinkDemodDecodeConfig.decode_config required"
        )
    return out
