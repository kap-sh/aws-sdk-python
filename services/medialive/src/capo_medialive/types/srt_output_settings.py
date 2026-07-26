"""Generated from Smithy shape ``com.amazonaws.medialive#SrtOutputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0_max10000
    import capo_medialive.types.__integer_min40_max16000
    import capo_medialive.types.output_location_ref
    import capo_medialive.types.srt_encryption_type
    import capo_medialive.types.udp_container_settings


class SrtOutputSettings(TypedDict, closed=True):
    buffer_msec: NotRequired[
        "capo_medialive.types.__integer_min0_max10000.__integerMin0Max10000"
    ]
    """SRT output buffering in milliseconds. A higher value increases latency through the encoder. But the benefits are that it helps to maintain a constant, low-jitter SRT output, and it accommodates clock recovery, input switching, input disruptions, picture reordering, and so on. Range: 0-10000 milliseconds."""
    container_settings: NotRequired[
        "capo_medialive.types.udp_container_settings.UdpContainerSettings"
    ]
    destination: NotRequired[
        "capo_medialive.types.output_location_ref.OutputLocationRef"
    ]
    encryption_type: NotRequired[
        "capo_medialive.types.srt_encryption_type.SrtEncryptionType"
    ]
    """The encryption level for the content. Valid values are AES128, AES192, AES256. You and the downstream system should plan how to set this field because the values must not conflict with each other."""
    latency: NotRequired[
        "capo_medialive.types.__integer_min40_max16000.__integerMin40Max16000"
    ]
    """The latency value, in milliseconds, that is proposed during the SRT connection handshake. SRT will choose the maximum of the values proposed by the sender and receiver. On the sender side, latency is the amount of time a packet is held to give it a chance to be delivered successfully. On the receiver side, latency is the amount of time the packet is held before delivering to the application, aiding in packet recovery and matching as closely as possible the packet timing of the sender. Range: 40-16000 milliseconds."""


# --- restJson1 ser/de ---
def serialize_json(value: SrtOutputSettings) -> dict:
    out: dict = {}
    if "buffer_msec" in value:
        out["bufferMsec"] = value["buffer_msec"]
    if "container_settings" in value:
        import capo_medialive.types.udp_container_settings

        out["containerSettings"] = (
            capo_medialive.types.udp_container_settings.serialize_json(
                value["container_settings"]
            )
        )
    if "destination" in value:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    if "encryption_type" in value:
        import capo_medialive.types.srt_encryption_type

        out["encryptionType"] = capo_medialive.types.srt_encryption_type.serialize_json(
            value["encryption_type"]
        )
    if "latency" in value:
        out["latency"] = value["latency"]
    return out


def deserialize_json(data: dict) -> SrtOutputSettings:
    out: SrtOutputSettings = {}  # type: ignore[typeddict-item]
    if "bufferMsec" in data:
        out["buffer_msec"] = data["bufferMsec"]
    if "containerSettings" in data:
        import capo_medialive.types.udp_container_settings

        out["container_settings"] = (
            capo_medialive.types.udp_container_settings.deserialize_json(
                data["containerSettings"]
            )
        )
    if "destination" in data:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.deserialize_json(
            data["destination"]
        )
    if "encryptionType" in data:
        import capo_medialive.types.srt_encryption_type

        out["encryption_type"] = (
            capo_medialive.types.srt_encryption_type.deserialize_json(
                data["encryptionType"]
            )
        )
    if "latency" in data:
        out["latency"] = data["latency"]
    return out
