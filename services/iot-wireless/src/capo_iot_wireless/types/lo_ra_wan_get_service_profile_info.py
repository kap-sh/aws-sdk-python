"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANGetServiceProfileInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.add_gw_metadata
    import capo_iot_wireless.types.channel_mask
    import capo_iot_wireless.types.dev_status_req_freq
    import capo_iot_wireless.types.dl_bucket_size
    import capo_iot_wireless.types.dl_rate
    import capo_iot_wireless.types.dl_rate_policy
    import capo_iot_wireless.types.dr_max
    import capo_iot_wireless.types.dr_min
    import capo_iot_wireless.types.hr_allowed
    import capo_iot_wireless.types.min_gw_diversity
    import capo_iot_wireless.types.nb_trans_max
    import capo_iot_wireless.types.nb_trans_min
    import capo_iot_wireless.types.nwk_geo_loc
    import capo_iot_wireless.types.pr_allowed
    import capo_iot_wireless.types.ra_allowed
    import capo_iot_wireless.types.report_dev_status_battery
    import capo_iot_wireless.types.report_dev_status_margin
    import capo_iot_wireless.types.target_per
    import capo_iot_wireless.types.tx_power_index_max
    import capo_iot_wireless.types.tx_power_index_min
    import capo_iot_wireless.types.ul_bucket_size
    import capo_iot_wireless.types.ul_rate
    import capo_iot_wireless.types.ul_rate_policy


class LoRaWANGetServiceProfileInfo(TypedDict, closed=True):
    ul_rate: NotRequired["capo_iot_wireless.types.ul_rate.UlRate"]
    """<p>The ULRate value.</p>"""
    ul_bucket_size: NotRequired["capo_iot_wireless.types.ul_bucket_size.UlBucketSize"]
    """<p>The ULBucketSize value.</p>"""
    ul_rate_policy: NotRequired["capo_iot_wireless.types.ul_rate_policy.UlRatePolicy"]
    """<p>The ULRatePolicy value.</p>"""
    dl_rate: NotRequired["capo_iot_wireless.types.dl_rate.DlRate"]
    """<p>The DLRate value.</p>"""
    dl_bucket_size: NotRequired["capo_iot_wireless.types.dl_bucket_size.DlBucketSize"]
    """<p>The DLBucketSize value.</p>"""
    dl_rate_policy: NotRequired["capo_iot_wireless.types.dl_rate_policy.DlRatePolicy"]
    """<p>The DLRatePolicy value.</p>"""
    add_gw_metadata: "capo_iot_wireless.types.add_gw_metadata.AddGwMetadata"
    """<p>The AddGWMetaData value.</p>"""
    dev_status_req_freq: NotRequired[
        "capo_iot_wireless.types.dev_status_req_freq.DevStatusReqFreq"
    ]
    """<p>The DevStatusReqFreq value.</p>"""
    report_dev_status_battery: (
        "capo_iot_wireless.types.report_dev_status_battery.ReportDevStatusBattery"
    )
    """<p>The ReportDevStatusBattery value.</p>"""
    report_dev_status_margin: (
        "capo_iot_wireless.types.report_dev_status_margin.ReportDevStatusMargin"
    )
    """<p>The ReportDevStatusMargin value.</p>"""
    dr_min: "capo_iot_wireless.types.dr_min.DrMin"
    """<p>The DRMin value.</p>"""
    dr_max: "capo_iot_wireless.types.dr_max.DrMax"
    """<p>The DRMax value.</p>"""
    channel_mask: NotRequired["capo_iot_wireless.types.channel_mask.ChannelMask"]
    """<p>The ChannelMask value.</p>"""
    pr_allowed: "capo_iot_wireless.types.pr_allowed.PrAllowed"
    """<p>The PRAllowed value that describes whether passive roaming is allowed.</p>"""
    hr_allowed: "capo_iot_wireless.types.hr_allowed.HrAllowed"
    """<p>The HRAllowed value that describes whether handover roaming is allowed.</p>"""
    ra_allowed: "capo_iot_wireless.types.ra_allowed.RaAllowed"
    """<p>The RAAllowed value that describes whether roaming activation is allowed.</p>"""
    nwk_geo_loc: "capo_iot_wireless.types.nwk_geo_loc.NwkGeoLoc"
    """<p>The NwkGeoLoc value.</p>"""
    target_per: "capo_iot_wireless.types.target_per.TargetPer"
    """<p>The TargetPER value.</p>"""
    min_gw_diversity: NotRequired[
        "capo_iot_wireless.types.min_gw_diversity.MinGwDiversity"
    ]
    """<p>The MinGwDiversity value.</p>"""
    tx_power_index_min: NotRequired[
        "capo_iot_wireless.types.tx_power_index_min.TxPowerIndexMin"
    ]
    """<p>The Transmit Power Index minimum value.</p> <p>Default: <code>0</code> </p>"""
    tx_power_index_max: NotRequired[
        "capo_iot_wireless.types.tx_power_index_max.TxPowerIndexMax"
    ]
    """<p>The Transmit Power Index maximum value.</p> <p>Default: <code>15</code> </p>"""
    nb_trans_min: NotRequired["capo_iot_wireless.types.nb_trans_min.NbTransMin"]
    """<p>The minimum number of transmissions.</p> <p>Default: <code>0</code> </p>"""
    nb_trans_max: NotRequired["capo_iot_wireless.types.nb_trans_max.NbTransMax"]
    """<p>The maximum number of transmissions.</p> <p>Default: <code>3</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANGetServiceProfileInfo) -> dict:
    out: dict = {}
    if "ul_rate" in value:
        out["UlRate"] = value["ul_rate"]
    if "ul_bucket_size" in value:
        out["UlBucketSize"] = value["ul_bucket_size"]
    if "ul_rate_policy" in value:
        out["UlRatePolicy"] = value["ul_rate_policy"]
    if "dl_rate" in value:
        out["DlRate"] = value["dl_rate"]
    if "dl_bucket_size" in value:
        out["DlBucketSize"] = value["dl_bucket_size"]
    if "dl_rate_policy" in value:
        out["DlRatePolicy"] = value["dl_rate_policy"]
    out["AddGwMetadata"] = value.get("add_gw_metadata", False)
    if "dev_status_req_freq" in value:
        out["DevStatusReqFreq"] = value["dev_status_req_freq"]
    out["ReportDevStatusBattery"] = value.get("report_dev_status_battery", False)
    out["ReportDevStatusMargin"] = value.get("report_dev_status_margin", False)
    out["DrMin"] = value.get("dr_min", 0)
    out["DrMax"] = value.get("dr_max", 0)
    if "channel_mask" in value:
        out["ChannelMask"] = value["channel_mask"]
    out["PrAllowed"] = value.get("pr_allowed", False)
    out["HrAllowed"] = value.get("hr_allowed", False)
    out["RaAllowed"] = value.get("ra_allowed", False)
    out["NwkGeoLoc"] = value.get("nwk_geo_loc", False)
    out["TargetPer"] = value.get("target_per", 0)
    if "min_gw_diversity" in value:
        out["MinGwDiversity"] = value["min_gw_diversity"]
    if "tx_power_index_min" in value:
        out["TxPowerIndexMin"] = value["tx_power_index_min"]
    if "tx_power_index_max" in value:
        out["TxPowerIndexMax"] = value["tx_power_index_max"]
    if "nb_trans_min" in value:
        out["NbTransMin"] = value["nb_trans_min"]
    if "nb_trans_max" in value:
        out["NbTransMax"] = value["nb_trans_max"]
    return out


def deserialize_json(data: dict) -> LoRaWANGetServiceProfileInfo:
    out: LoRaWANGetServiceProfileInfo = {}  # type: ignore[typeddict-item]
    if "UlRate" in data:
        out["ul_rate"] = data["UlRate"]
    if "UlBucketSize" in data:
        out["ul_bucket_size"] = data["UlBucketSize"]
    if "UlRatePolicy" in data:
        out["ul_rate_policy"] = data["UlRatePolicy"]
    if "DlRate" in data:
        out["dl_rate"] = data["DlRate"]
    if "DlBucketSize" in data:
        out["dl_bucket_size"] = data["DlBucketSize"]
    if "DlRatePolicy" in data:
        out["dl_rate_policy"] = data["DlRatePolicy"]
    if "AddGwMetadata" in data:
        out["add_gw_metadata"] = data["AddGwMetadata"]
    else:
        out["add_gw_metadata"] = False
    if "DevStatusReqFreq" in data:
        out["dev_status_req_freq"] = data["DevStatusReqFreq"]
    if "ReportDevStatusBattery" in data:
        out["report_dev_status_battery"] = data["ReportDevStatusBattery"]
    else:
        out["report_dev_status_battery"] = False
    if "ReportDevStatusMargin" in data:
        out["report_dev_status_margin"] = data["ReportDevStatusMargin"]
    else:
        out["report_dev_status_margin"] = False
    if "DrMin" in data:
        out["dr_min"] = data["DrMin"]
    else:
        out["dr_min"] = 0
    if "DrMax" in data:
        out["dr_max"] = data["DrMax"]
    else:
        out["dr_max"] = 0
    if "ChannelMask" in data:
        out["channel_mask"] = data["ChannelMask"]
    if "PrAllowed" in data:
        out["pr_allowed"] = data["PrAllowed"]
    else:
        out["pr_allowed"] = False
    if "HrAllowed" in data:
        out["hr_allowed"] = data["HrAllowed"]
    else:
        out["hr_allowed"] = False
    if "RaAllowed" in data:
        out["ra_allowed"] = data["RaAllowed"]
    else:
        out["ra_allowed"] = False
    if "NwkGeoLoc" in data:
        out["nwk_geo_loc"] = data["NwkGeoLoc"]
    else:
        out["nwk_geo_loc"] = False
    if "TargetPer" in data:
        out["target_per"] = data["TargetPer"]
    else:
        out["target_per"] = 0
    if "MinGwDiversity" in data:
        out["min_gw_diversity"] = data["MinGwDiversity"]
    if "TxPowerIndexMin" in data:
        out["tx_power_index_min"] = data["TxPowerIndexMin"]
    if "TxPowerIndexMax" in data:
        out["tx_power_index_max"] = data["TxPowerIndexMax"]
    if "NbTransMin" in data:
        out["nb_trans_min"] = data["NbTransMin"]
    if "NbTransMax" in data:
        out["nb_trans_max"] = data["NbTransMax"]
    return out
