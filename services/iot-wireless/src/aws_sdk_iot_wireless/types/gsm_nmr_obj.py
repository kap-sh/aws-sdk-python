"""Generated from Smithy shape ``com.amazonaws.iotwireless#GsmNmrObj``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.bcch
    import aws_sdk_iot_wireless.types.bsic
    import aws_sdk_iot_wireless.types.global_identity
    import aws_sdk_iot_wireless.types.rx_level


class GsmNmrObj(TypedDict):
    bsic: "aws_sdk_iot_wireless.types.bsic.BSIC"
    """<p>GSM base station identity code (BSIC).</p>"""
    bcch: "aws_sdk_iot_wireless.types.bcch.BCCH"
    """<p>GSM broadcast control channel.</p>"""
    rx_level: NotRequired["aws_sdk_iot_wireless.types.rx_level.RxLevel"]
    """<p>Rx level, which is the received signal power, measured in dBm (decibel-milliwatts).</p>"""
    global_identity: NotRequired[
        "aws_sdk_iot_wireless.types.global_identity.GlobalIdentity"
    ]
    """<p>Global identity information of the GSM object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GsmNmrObj) -> dict:
    out: dict = {}
    out["Bsic"] = value["bsic"]
    out["Bcch"] = value["bcch"]
    if "rx_level" in value:
        out["RxLevel"] = value["rx_level"]
    if "global_identity" in value:
        import aws_sdk_iot_wireless.types.global_identity

        out["GlobalIdentity"] = (
            aws_sdk_iot_wireless.types.global_identity.serialize_json(
                value["global_identity"]
            )
        )
    return out


def deserialize_json(data: dict) -> GsmNmrObj:
    out: GsmNmrObj = {}  # type: ignore[typeddict-item]
    if "Bsic" in data:
        out["bsic"] = data["Bsic"]
    else:
        raise DeserializationError("GsmNmrObj.bsic required")
    if "Bcch" in data:
        out["bcch"] = data["Bcch"]
    else:
        raise DeserializationError("GsmNmrObj.bcch required")
    if "RxLevel" in data:
        out["rx_level"] = data["RxLevel"]
    if "GlobalIdentity" in data:
        import aws_sdk_iot_wireless.types.global_identity

        out["global_identity"] = (
            aws_sdk_iot_wireless.types.global_identity.deserialize_json(
                data["GlobalIdentity"]
            )
        )
    return out
