"""Generated from Smithy shape ``com.amazonaws.iotwireless#GlobalIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.geran_cid
    import aws_sdk_iot_wireless.types.lac


class GlobalIdentity(TypedDict, closed=True):
    lac: "aws_sdk_iot_wireless.types.lac.LAC"
    """<p>Location area code of the global identity.</p>"""
    geran_cid: "aws_sdk_iot_wireless.types.geran_cid.GeranCid"
    """<p>GERAN (GSM EDGE Radio Access Network) cell global identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlobalIdentity) -> dict:
    out: dict = {}
    out["Lac"] = value["lac"]
    out["GeranCid"] = value["geran_cid"]
    return out


def deserialize_json(data: dict) -> GlobalIdentity:
    out: GlobalIdentity = {}  # type: ignore[typeddict-item]
    if "Lac" in data:
        out["lac"] = data["Lac"]
    else:
        raise DeserializationError("GlobalIdentity.lac required")
    if "GeranCid" in data:
        out["geran_cid"] = data["GeranCid"]
    else:
        raise DeserializationError("GlobalIdentity.geran_cid required")
    return out
