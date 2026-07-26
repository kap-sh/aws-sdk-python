"""Generated from Smithy shape ``com.amazonaws.groundstation#AntennaUplinkConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.eirp
    import capo_groundstation.types.uplink_spectrum_config


class AntennaUplinkConfig(TypedDict, closed=True):
    transmit_disabled: NotRequired["bool"]
    """<p>Whether or not uplink transmit is disabled.</p>"""
    spectrum_config: (
        "capo_groundstation.types.uplink_spectrum_config.UplinkSpectrumConfig"
    )
    """<p>Information about the uplink spectral <code>Config</code>.</p>"""
    target_eirp: "capo_groundstation.types.eirp.Eirp"
    """<p>EIRP of the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AntennaUplinkConfig) -> dict:
    out: dict = {}
    if "transmit_disabled" in value:
        out["transmitDisabled"] = value["transmit_disabled"]
    import capo_groundstation.types.uplink_spectrum_config

    out["spectrumConfig"] = (
        capo_groundstation.types.uplink_spectrum_config.serialize_json(
            value["spectrum_config"]
        )
    )
    import capo_groundstation.types.eirp

    out["targetEirp"] = capo_groundstation.types.eirp.serialize_json(
        value["target_eirp"]
    )
    return out


def deserialize_json(data: dict) -> AntennaUplinkConfig:
    out: AntennaUplinkConfig = {}  # type: ignore[typeddict-item]
    if "transmitDisabled" in data:
        out["transmit_disabled"] = data["transmitDisabled"]
    if "spectrumConfig" in data:
        import capo_groundstation.types.uplink_spectrum_config

        out["spectrum_config"] = (
            capo_groundstation.types.uplink_spectrum_config.deserialize_json(
                data["spectrumConfig"]
            )
        )
    else:
        raise DeserializationError("AntennaUplinkConfig.spectrum_config required")
    if "targetEirp" in data:
        import capo_groundstation.types.eirp

        out["target_eirp"] = capo_groundstation.types.eirp.deserialize_json(
            data["targetEirp"]
        )
    else:
        raise DeserializationError("AntennaUplinkConfig.target_eirp required")
    return out
