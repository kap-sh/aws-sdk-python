"""Generated from Smithy shape ``com.amazonaws.iotwireless#LoRaWANDeviceProfile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.class_b_timeout
    import aws_sdk_iot_wireless.types.class_c_timeout
    import aws_sdk_iot_wireless.types.factory_preset_freqs_list
    import aws_sdk_iot_wireless.types.mac_version
    import aws_sdk_iot_wireless.types.max_duty_cycle
    import aws_sdk_iot_wireless.types.max_eirp
    import aws_sdk_iot_wireless.types.ping_slot_dr
    import aws_sdk_iot_wireless.types.ping_slot_freq
    import aws_sdk_iot_wireless.types.ping_slot_period
    import aws_sdk_iot_wireless.types.reg_params_revision
    import aws_sdk_iot_wireless.types.rf_region
    import aws_sdk_iot_wireless.types.rx_data_rate2
    import aws_sdk_iot_wireless.types.rx_delay1
    import aws_sdk_iot_wireless.types.rx_dr_offset1
    import aws_sdk_iot_wireless.types.rx_freq2
    import aws_sdk_iot_wireless.types.supports32_bit_f_cnt
    import aws_sdk_iot_wireless.types.supports_class_b
    import aws_sdk_iot_wireless.types.supports_class_c
    import aws_sdk_iot_wireless.types.supports_join


class LoRaWANDeviceProfile(TypedDict):
    supports_class_b: "aws_sdk_iot_wireless.types.supports_class_b.SupportsClassB"
    """<p>The SupportsClassB value.</p>"""
    class_b_timeout: NotRequired[
        "aws_sdk_iot_wireless.types.class_b_timeout.ClassBTimeout"
    ]
    """<p>The ClassBTimeout value.</p>"""
    ping_slot_period: NotRequired[
        "aws_sdk_iot_wireless.types.ping_slot_period.PingSlotPeriod"
    ]
    """<p>The PingSlotPeriod value.</p>"""
    ping_slot_dr: NotRequired["aws_sdk_iot_wireless.types.ping_slot_dr.PingSlotDr"]
    """<p>The PingSlotDR value.</p>"""
    ping_slot_freq: NotRequired[
        "aws_sdk_iot_wireless.types.ping_slot_freq.PingSlotFreq"
    ]
    """<p>The PingSlotFreq value.</p>"""
    supports_class_c: "aws_sdk_iot_wireless.types.supports_class_c.SupportsClassC"
    """<p>The SupportsClassC value.</p>"""
    class_c_timeout: NotRequired[
        "aws_sdk_iot_wireless.types.class_c_timeout.ClassCTimeout"
    ]
    """<p>The ClassCTimeout value.</p>"""
    mac_version: NotRequired["aws_sdk_iot_wireless.types.mac_version.MacVersion"]
    """<p>The MAC version (such as OTAA 1.1 or OTAA 1.0.3) to use with this device profile.</p>"""
    reg_params_revision: NotRequired[
        "aws_sdk_iot_wireless.types.reg_params_revision.RegParamsRevision"
    ]
    """<p>The version of regional parameters.</p>"""
    rx_delay1: NotRequired["aws_sdk_iot_wireless.types.rx_delay1.RxDelay1"]
    """<p>The RXDelay1 value.</p>"""
    rx_dr_offset1: NotRequired["aws_sdk_iot_wireless.types.rx_dr_offset1.RxDrOffset1"]
    """<p>The RXDROffset1 value.</p>"""
    rx_data_rate2: NotRequired["aws_sdk_iot_wireless.types.rx_data_rate2.RxDataRate2"]
    """<p>The RXDataRate2 value.</p>"""
    rx_freq2: NotRequired["aws_sdk_iot_wireless.types.rx_freq2.RxFreq2"]
    """<p>The RXFreq2 value.</p>"""
    factory_preset_freqs_list: NotRequired[
        "aws_sdk_iot_wireless.types.factory_preset_freqs_list.FactoryPresetFreqsList"
    ]
    """<p>The list of values that make up the FactoryPresetFreqs value.</p>"""
    max_eirp: NotRequired["aws_sdk_iot_wireless.types.max_eirp.MaxEirp"]
    """<p>The MaxEIRP value.</p>"""
    max_duty_cycle: NotRequired[
        "aws_sdk_iot_wireless.types.max_duty_cycle.MaxDutyCycle"
    ]
    """<p>The MaxDutyCycle value. It ranges from 0 to 15.</p>"""
    rf_region: NotRequired["aws_sdk_iot_wireless.types.rf_region.RfRegion"]
    """<p>The frequency band (RFRegion) value.</p>"""
    supports_join: NotRequired["aws_sdk_iot_wireless.types.supports_join.SupportsJoin"]
    """<p>The SupportsJoin value.</p>"""
    supports32_bit_f_cnt: (
        "aws_sdk_iot_wireless.types.supports32_bit_f_cnt.Supports32BitFCnt"
    )
    """<p>The Supports32BitFCnt value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoRaWANDeviceProfile) -> dict:
    out: dict = {}
    out["SupportsClassB"] = value.get("supports_class_b", False)
    if "class_b_timeout" in value:
        out["ClassBTimeout"] = value["class_b_timeout"]
    if "ping_slot_period" in value:
        out["PingSlotPeriod"] = value["ping_slot_period"]
    if "ping_slot_dr" in value:
        out["PingSlotDr"] = value["ping_slot_dr"]
    if "ping_slot_freq" in value:
        out["PingSlotFreq"] = value["ping_slot_freq"]
    out["SupportsClassC"] = value.get("supports_class_c", False)
    if "class_c_timeout" in value:
        out["ClassCTimeout"] = value["class_c_timeout"]
    if "mac_version" in value:
        out["MacVersion"] = value["mac_version"]
    if "reg_params_revision" in value:
        out["RegParamsRevision"] = value["reg_params_revision"]
    if "rx_delay1" in value:
        out["RxDelay1"] = value["rx_delay1"]
    if "rx_dr_offset1" in value:
        out["RxDrOffset1"] = value["rx_dr_offset1"]
    if "rx_data_rate2" in value:
        out["RxDataRate2"] = value["rx_data_rate2"]
    if "rx_freq2" in value:
        out["RxFreq2"] = value["rx_freq2"]
    if "factory_preset_freqs_list" in value:
        import aws_sdk_iot_wireless.types.factory_preset_freqs_list

        out["FactoryPresetFreqsList"] = (
            aws_sdk_iot_wireless.types.factory_preset_freqs_list.serialize_json(
                value["factory_preset_freqs_list"]
            )
        )
    if "max_eirp" in value:
        out["MaxEirp"] = value["max_eirp"]
    if "max_duty_cycle" in value:
        out["MaxDutyCycle"] = value["max_duty_cycle"]
    if "rf_region" in value:
        out["RfRegion"] = value["rf_region"]
    if "supports_join" in value:
        out["SupportsJoin"] = value["supports_join"]
    out["Supports32BitFCnt"] = value.get("supports32_bit_f_cnt", False)
    return out


def deserialize_json(data: dict) -> LoRaWANDeviceProfile:
    out: LoRaWANDeviceProfile = {}  # type: ignore[typeddict-item]
    if "SupportsClassB" in data:
        out["supports_class_b"] = data["SupportsClassB"]
    else:
        out["supports_class_b"] = False
    if "ClassBTimeout" in data:
        out["class_b_timeout"] = data["ClassBTimeout"]
    if "PingSlotPeriod" in data:
        out["ping_slot_period"] = data["PingSlotPeriod"]
    if "PingSlotDr" in data:
        out["ping_slot_dr"] = data["PingSlotDr"]
    if "PingSlotFreq" in data:
        out["ping_slot_freq"] = data["PingSlotFreq"]
    if "SupportsClassC" in data:
        out["supports_class_c"] = data["SupportsClassC"]
    else:
        out["supports_class_c"] = False
    if "ClassCTimeout" in data:
        out["class_c_timeout"] = data["ClassCTimeout"]
    if "MacVersion" in data:
        out["mac_version"] = data["MacVersion"]
    if "RegParamsRevision" in data:
        out["reg_params_revision"] = data["RegParamsRevision"]
    if "RxDelay1" in data:
        out["rx_delay1"] = data["RxDelay1"]
    if "RxDrOffset1" in data:
        out["rx_dr_offset1"] = data["RxDrOffset1"]
    if "RxDataRate2" in data:
        out["rx_data_rate2"] = data["RxDataRate2"]
    if "RxFreq2" in data:
        out["rx_freq2"] = data["RxFreq2"]
    if "FactoryPresetFreqsList" in data:
        import aws_sdk_iot_wireless.types.factory_preset_freqs_list

        out["factory_preset_freqs_list"] = (
            aws_sdk_iot_wireless.types.factory_preset_freqs_list.deserialize_json(
                data["FactoryPresetFreqsList"]
            )
        )
    if "MaxEirp" in data:
        out["max_eirp"] = data["MaxEirp"]
    if "MaxDutyCycle" in data:
        out["max_duty_cycle"] = data["MaxDutyCycle"]
    if "RfRegion" in data:
        out["rf_region"] = data["RfRegion"]
    if "SupportsJoin" in data:
        out["supports_join"] = data["SupportsJoin"]
    if "Supports32BitFCnt" in data:
        out["supports32_bit_f_cnt"] = data["Supports32BitFCnt"]
    else:
        out["supports32_bit_f_cnt"] = False
    return out
