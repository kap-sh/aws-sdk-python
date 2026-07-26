"""Generated from Smithy shape ``com.amazonaws.groundstation#AntennaDownlinkDemodDecodeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.decode_config
    import capo_groundstation.types.demodulation_config
    import capo_groundstation.types.spectrum_config


class AntennaDownlinkDemodDecodeConfig(TypedDict, closed=True):
    spectrum_config: "capo_groundstation.types.spectrum_config.SpectrumConfig"
    """<p>Information about the spectral <code>Config</code>.</p>"""
    demodulation_config: (
        "capo_groundstation.types.demodulation_config.DemodulationConfig"
    )
    """<p>Information about the demodulation <code>Config</code>.</p>"""
    decode_config: "capo_groundstation.types.decode_config.DecodeConfig"
    """<p>Information about the decode <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AntennaDownlinkDemodDecodeConfig) -> dict:
    out: dict = {}
    import capo_groundstation.types.spectrum_config

    out["spectrumConfig"] = capo_groundstation.types.spectrum_config.serialize_json(
        value["spectrum_config"]
    )
    import capo_groundstation.types.demodulation_config

    out["demodulationConfig"] = (
        capo_groundstation.types.demodulation_config.serialize_json(
            value["demodulation_config"]
        )
    )
    import capo_groundstation.types.decode_config

    out["decodeConfig"] = capo_groundstation.types.decode_config.serialize_json(
        value["decode_config"]
    )
    return out


def deserialize_json(data: dict) -> AntennaDownlinkDemodDecodeConfig:
    out: AntennaDownlinkDemodDecodeConfig = {}  # type: ignore[typeddict-item]
    if "spectrumConfig" in data:
        import capo_groundstation.types.spectrum_config

        out["spectrum_config"] = (
            capo_groundstation.types.spectrum_config.deserialize_json(
                data["spectrumConfig"]
            )
        )
    else:
        raise DeserializationError(
            "AntennaDownlinkDemodDecodeConfig.spectrum_config required"
        )
    if "demodulationConfig" in data:
        import capo_groundstation.types.demodulation_config

        out["demodulation_config"] = (
            capo_groundstation.types.demodulation_config.deserialize_json(
                data["demodulationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "AntennaDownlinkDemodDecodeConfig.demodulation_config required"
        )
    if "decodeConfig" in data:
        import capo_groundstation.types.decode_config

        out["decode_config"] = capo_groundstation.types.decode_config.deserialize_json(
            data["decodeConfig"]
        )
    else:
        raise DeserializationError(
            "AntennaDownlinkDemodDecodeConfig.decode_config required"
        )
    return out
