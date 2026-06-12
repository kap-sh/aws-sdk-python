"""Generated from Smithy shape ``com.amazonaws.groundstation#AntennaDownlinkConfig``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_groundstation.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_groundstation.types.spectrum_config

class AntennaDownlinkConfig(TypedDict):
    spectrum_config: "aws_sdk_groundstation.types.spectrum_config.SpectrumConfig"
    """<p>Object that describes a spectral <code>Config</code>.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AntennaDownlinkConfig) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.spectrum_config
    out["spectrumConfig"] = aws_sdk_groundstation.types.spectrum_config.serialize_json(value["spectrum_config"])
    return out


def deserialize_json(data: dict) -> AntennaDownlinkConfig:
    out: AntennaDownlinkConfig = {}  # type: ignore[typeddict-item]
    if "spectrumConfig" in data:
        import aws_sdk_groundstation.types.spectrum_config
        out["spectrum_config"] = aws_sdk_groundstation.types.spectrum_config.deserialize_json(data["spectrumConfig"])
    else:
        raise DeserializationError("AntennaDownlinkConfig.spectrum_config required")
    return out