"""Generated from Smithy shape ``com.amazonaws.groundstation#AntennaDownlinkConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.spectrum_config


class AntennaDownlinkConfig(TypedDict, closed=True):
    spectrum_config: "capo_groundstation.types.spectrum_config.SpectrumConfig"
    """<p>Object that describes a spectral <code>Config</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AntennaDownlinkConfig) -> dict:
    out: dict = {}
    import capo_groundstation.types.spectrum_config

    out["spectrumConfig"] = capo_groundstation.types.spectrum_config.serialize_json(
        value["spectrum_config"]
    )
    return out


def deserialize_json(data: dict) -> AntennaDownlinkConfig:
    out: AntennaDownlinkConfig = {}  # type: ignore[typeddict-item]
    if "spectrumConfig" in data:
        import capo_groundstation.types.spectrum_config

        out["spectrum_config"] = (
            capo_groundstation.types.spectrum_config.deserialize_json(
                data["spectrumConfig"]
            )
        )
    else:
        raise DeserializationError("AntennaDownlinkConfig.spectrum_config required")
    return out
