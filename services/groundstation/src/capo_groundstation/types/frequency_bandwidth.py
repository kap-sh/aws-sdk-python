"""Generated from Smithy shape ``com.amazonaws.groundstation#FrequencyBandwidth``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.bandwidth_units


class FrequencyBandwidth(TypedDict, closed=True):
    value: "float"
    """<p>Frequency bandwidth value. AWS Ground Station currently has the following bandwidth limitations:</p> <ul> <li> <p>For <code>AntennaDownlinkDemodDecodeconfig</code>, valid values are between 125 kHz to 650 MHz.</p> </li> <li> <p>For <code>AntennaDownlinkconfig</code>, valid values are between 10 kHz to 54 MHz.</p> </li> <li> <p>For <code>AntennaUplinkConfig</code>, valid values are between 10 kHz to 54 MHz.</p> </li> </ul>"""
    units: "capo_groundstation.types.bandwidth_units.BandwidthUnits"
    """<p>Frequency bandwidth units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrequencyBandwidth) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    import capo_groundstation.types.bandwidth_units

    out["units"] = capo_groundstation.types.bandwidth_units.serialize_json(
        value["units"]
    )
    return out


def deserialize_json(data: dict) -> FrequencyBandwidth:
    out: FrequencyBandwidth = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("FrequencyBandwidth.value required")
    if "units" in data:
        import capo_groundstation.types.bandwidth_units

        out["units"] = capo_groundstation.types.bandwidth_units.deserialize_json(
            data["units"]
        )
    else:
        raise DeserializationError("FrequencyBandwidth.units required")
    return out
