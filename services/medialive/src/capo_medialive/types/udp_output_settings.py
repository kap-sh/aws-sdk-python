"""Generated from Smithy shape ``com.amazonaws.medialive#UdpOutputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0_max10000
    import capo_medialive.types.fec_output_settings
    import capo_medialive.types.output_location_ref
    import capo_medialive.types.udp_container_settings


class UdpOutputSettings(TypedDict, closed=True):
    buffer_msec: NotRequired[
        "capo_medialive.types.__integer_min0_max10000.__integerMin0Max10000"
    ]
    """UDP output buffering in milliseconds. Larger values increase latency through the transcoder but simultaneously assist the transcoder in maintaining a constant, low-jitter UDP/RTP output while accommodating clock recovery, input switching, input disruptions, picture reordering, etc."""
    container_settings: NotRequired[
        "capo_medialive.types.udp_container_settings.UdpContainerSettings"
    ]
    destination: NotRequired[
        "capo_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """Destination address and port number for RTP or UDP packets. Can be unicast or multicast RTP or UDP (eg. rtp://239.10.10.10:5001 or udp://10.100.100.100:5002)."""
    fec_output_settings: NotRequired[
        "capo_medialive.types.fec_output_settings.FecOutputSettings"
    ]
    """Settings for enabling and adjusting Forward Error Correction on UDP outputs."""


# --- restJson1 ser/de ---
def serialize_json(value: UdpOutputSettings) -> dict:
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
    if "fec_output_settings" in value:
        import capo_medialive.types.fec_output_settings

        out["fecOutputSettings"] = (
            capo_medialive.types.fec_output_settings.serialize_json(
                value["fec_output_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UdpOutputSettings:
    out: UdpOutputSettings = {}  # type: ignore[typeddict-item]
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
    if "fecOutputSettings" in data:
        import capo_medialive.types.fec_output_settings

        out["fec_output_settings"] = (
            capo_medialive.types.fec_output_settings.deserialize_json(
                data["fecOutputSettings"]
            )
        )
    return out
