"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANServiceProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.add_gw_metadata
    import capo_iot_wireless.types.dr_max_box
    import capo_iot_wireless.types.dr_min_box
    import capo_iot_wireless.types.nb_trans_max
    import capo_iot_wireless.types.nb_trans_min
    import capo_iot_wireless.types.pr_allowed
    import capo_iot_wireless.types.ra_allowed
    import capo_iot_wireless.types.tx_power_index_max
    import capo_iot_wireless.types.tx_power_index_min


class LoRaWANServiceProfile(TypedDict, closed=True):
    add_gw_metadata: "capo_iot_wireless.types.add_gw_metadata.AddGwMetadata"
    """<p>The AddGWMetaData value.</p>"""
    dr_min: NotRequired["capo_iot_wireless.types.dr_min_box.DrMinBox"]
    """<p>The DrMin value.</p>"""
    dr_max: NotRequired["capo_iot_wireless.types.dr_max_box.DrMaxBox"]
    """<p>The DrMax value.</p>"""
    pr_allowed: "capo_iot_wireless.types.pr_allowed.PrAllowed"
    """<p>The PRAllowed value that describes whether passive roaming is allowed.</p>"""
    ra_allowed: "capo_iot_wireless.types.ra_allowed.RaAllowed"
    """<p>The RAAllowed value that describes whether roaming activation is allowed.</p>"""
    tx_power_index_min: NotRequired[
        "capo_iot_wireless.types.tx_power_index_min.TxPowerIndexMin"
    ]
    """<p>The Transmit Power Index minimum.</p> <p>Default: <code>0</code> </p>"""
    tx_power_index_max: NotRequired[
        "capo_iot_wireless.types.tx_power_index_max.TxPowerIndexMax"
    ]
    """<p>The Transmit Power Index maximum.</p> <p>Default: <code>15</code> </p>"""
    nb_trans_min: NotRequired["capo_iot_wireless.types.nb_trans_min.NbTransMin"]
    """<p>The minimum number of transmissions.</p> <p>Default: <code>0</code> </p>"""
    nb_trans_max: NotRequired["capo_iot_wireless.types.nb_trans_max.NbTransMax"]
    """<p>The maximum number of transmissions.</p> <p>Default: <code>3</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANServiceProfile) -> dict:
    out: dict = {}
    out["AddGwMetadata"] = value.get("add_gw_metadata", False)
    if "dr_min" in value:
        out["DrMin"] = value["dr_min"]
    if "dr_max" in value:
        out["DrMax"] = value["dr_max"]
    out["PrAllowed"] = value.get("pr_allowed", False)
    out["RaAllowed"] = value.get("ra_allowed", False)
    if "tx_power_index_min" in value:
        out["TxPowerIndexMin"] = value["tx_power_index_min"]
    if "tx_power_index_max" in value:
        out["TxPowerIndexMax"] = value["tx_power_index_max"]
    if "nb_trans_min" in value:
        out["NbTransMin"] = value["nb_trans_min"]
    if "nb_trans_max" in value:
        out["NbTransMax"] = value["nb_trans_max"]
    return out


def deserialize_json(data: dict) -> LoRaWANServiceProfile:
    out: LoRaWANServiceProfile = {}  # type: ignore[typeddict-item]
    if "AddGwMetadata" in data:
        out["add_gw_metadata"] = data["AddGwMetadata"]
    else:
        out["add_gw_metadata"] = False
    if "DrMin" in data:
        out["dr_min"] = data["DrMin"]
    if "DrMax" in data:
        out["dr_max"] = data["DrMax"]
    if "PrAllowed" in data:
        out["pr_allowed"] = data["PrAllowed"]
    else:
        out["pr_allowed"] = False
    if "RaAllowed" in data:
        out["ra_allowed"] = data["RaAllowed"]
    else:
        out["ra_allowed"] = False
    if "TxPowerIndexMin" in data:
        out["tx_power_index_min"] = data["TxPowerIndexMin"]
    if "TxPowerIndexMax" in data:
        out["tx_power_index_max"] = data["TxPowerIndexMax"]
    if "NbTransMin" in data:
        out["nb_trans_min"] = data["NbTransMin"]
    if "NbTransMax" in data:
        out["nb_trans_max"] = data["NbTransMax"]
    return out
