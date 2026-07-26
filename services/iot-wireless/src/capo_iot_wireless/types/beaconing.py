"""Generated from Smithy shape ``com.amazonaws.iotwireless#Beaconing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.beaconing_data_rate
    import capo_iot_wireless.types.beaconing_frequencies


class Beaconing(TypedDict, closed=True):
    data_rate: NotRequired[
        "capo_iot_wireless.types.beaconing_data_rate.BeaconingDataRate"
    ]
    """<p>The data rate for gateways that are sending the beacons.</p>"""
    frequencies: NotRequired[
        "capo_iot_wireless.types.beaconing_frequencies.BeaconingFrequencies"
    ]
    """<p>The frequency list for the gateways to send the beacons.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Beaconing) -> dict:
    out: dict = {}
    if "data_rate" in value:
        out["DataRate"] = value["data_rate"]
    if "frequencies" in value:
        import capo_iot_wireless.types.beaconing_frequencies

        out["Frequencies"] = (
            capo_iot_wireless.types.beaconing_frequencies.serialize_json(
                value["frequencies"]
            )
        )
    return out


def deserialize_json(data: dict) -> Beaconing:
    out: Beaconing = {}  # type: ignore[typeddict-item]
    if "DataRate" in data:
        out["data_rate"] = data["DataRate"]
    if "Frequencies" in data:
        import capo_iot_wireless.types.beaconing_frequencies

        out["frequencies"] = (
            capo_iot_wireless.types.beaconing_frequencies.deserialize_json(
                data["Frequencies"]
            )
        )
    return out
