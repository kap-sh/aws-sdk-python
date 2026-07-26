"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANMulticastSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.dl_dr
    import capo_iot_wireless.types.dl_freq
    import capo_iot_wireless.types.ping_slot_period
    import capo_iot_wireless.types.session_start_time_timestamp
    import capo_iot_wireless.types.session_timeout


class LoRaWANMulticastSession(TypedDict, closed=True):
    dl_dr: NotRequired["capo_iot_wireless.types.dl_dr.DlDr"]
    dl_freq: NotRequired["capo_iot_wireless.types.dl_freq.DlFreq"]
    session_start_time: NotRequired[
        "capo_iot_wireless.types.session_start_time_timestamp.SessionStartTimeTimestamp"
    ]
    session_timeout: NotRequired[
        "capo_iot_wireless.types.session_timeout.SessionTimeout"
    ]
    ping_slot_period: NotRequired[
        "capo_iot_wireless.types.ping_slot_period.PingSlotPeriod"
    ]
    """<p>The PingSlotPeriod value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANMulticastSession) -> dict:
    out: dict = {}
    if "dl_dr" in value:
        out["DlDr"] = value["dl_dr"]
    if "dl_freq" in value:
        out["DlFreq"] = value["dl_freq"]
    if "session_start_time" in value:
        import capo_iot_wireless.types.session_start_time_timestamp

        out["SessionStartTime"] = (
            capo_iot_wireless.types.session_start_time_timestamp.serialize_json(
                value["session_start_time"]
            )
        )
    if "session_timeout" in value:
        out["SessionTimeout"] = value["session_timeout"]
    if "ping_slot_period" in value:
        out["PingSlotPeriod"] = value["ping_slot_period"]
    return out


def deserialize_json(data: dict) -> LoRaWANMulticastSession:
    out: LoRaWANMulticastSession = {}  # type: ignore[typeddict-item]
    if "DlDr" in data:
        out["dl_dr"] = data["DlDr"]
    if "DlFreq" in data:
        out["dl_freq"] = data["DlFreq"]
    if "SessionStartTime" in data:
        import capo_iot_wireless.types.session_start_time_timestamp

        out["session_start_time"] = (
            capo_iot_wireless.types.session_start_time_timestamp.deserialize_json(
                data["SessionStartTime"]
            )
        )
    if "SessionTimeout" in data:
        out["session_timeout"] = data["SessionTimeout"]
    if "PingSlotPeriod" in data:
        out["ping_slot_period"] = data["PingSlotPeriod"]
    return out
