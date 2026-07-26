"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkSendDataToDevice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.ack_mode_retry_duration_secs
    import capo_iot_wireless.types.message_type
    import capo_iot_wireless.types.seq


class SidewalkSendDataToDevice(TypedDict, closed=True):
    seq: NotRequired["capo_iot_wireless.types.seq.Seq"]
    """<p>The sequence number.</p>"""
    message_type: NotRequired["capo_iot_wireless.types.message_type.MessageType"]
    ack_mode_retry_duration_secs: NotRequired[
        "capo_iot_wireless.types.ack_mode_retry_duration_secs.AckModeRetryDurationSecs"
    ]
    """<p>The duration of time in seconds to retry sending the ACK.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkSendDataToDevice) -> dict:
    out: dict = {}
    if "seq" in value:
        out["Seq"] = value["seq"]
    if "message_type" in value:
        import capo_iot_wireless.types.message_type

        out["MessageType"] = capo_iot_wireless.types.message_type.serialize_json(
            value["message_type"]
        )
    if "ack_mode_retry_duration_secs" in value:
        out["AckModeRetryDurationSecs"] = value["ack_mode_retry_duration_secs"]
    return out


def deserialize_json(data: dict) -> SidewalkSendDataToDevice:
    out: SidewalkSendDataToDevice = {}  # type: ignore[typeddict-item]
    if "Seq" in data:
        out["seq"] = data["Seq"]
    if "MessageType" in data:
        import capo_iot_wireless.types.message_type

        out["message_type"] = capo_iot_wireless.types.message_type.deserialize_json(
            data["MessageType"]
        )
    if "AckModeRetryDurationSecs" in data:
        out["ack_mode_retry_duration_secs"] = data["AckModeRetryDurationSecs"]
    return out
