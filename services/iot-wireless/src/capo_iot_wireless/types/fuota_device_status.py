"""Generated from Smithy shape ``com.amazonaws.iotwireless#FuotaDeviceStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a wireless device in a FUOTA task.</p>"""
FuotaDeviceStatus: TypeAlias = Literal[
    "Initial",
    "Package_Not_Supported",
    "FragAlgo_unsupported",
    "Not_enough_memory",
    "FragIndex_unsupported",
    "Wrong_descriptor",
    "SessionCnt_replay",
    "MissingFrag",
    "MemoryError",
    "MICError",
    "Successful",
    "Device_exist_in_conflict_fuota_task",
]


# --- restJson1 ser/de ---
def serialize_json(value: FuotaDeviceStatus) -> str:
    return value


def deserialize_json(data: str) -> FuotaDeviceStatus:
    return cast(FuotaDeviceStatus, data)
