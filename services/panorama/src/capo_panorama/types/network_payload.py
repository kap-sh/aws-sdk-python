"""Generated from Smithy shape ``com.amazonaws.panorama#NetworkPayload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.ethernet_payload
    import capo_panorama.types.ntp_payload


class NetworkPayload(TypedDict, closed=True):
    ethernet0: NotRequired["capo_panorama.types.ethernet_payload.EthernetPayload"]
    """<p>Settings for Ethernet port 0.</p>"""
    ethernet1: NotRequired["capo_panorama.types.ethernet_payload.EthernetPayload"]
    """<p>Settings for Ethernet port 1.</p>"""
    ntp: NotRequired["capo_panorama.types.ntp_payload.NtpPayload"]
    """<p>Network time protocol (NTP) server settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkPayload) -> dict:
    out: dict = {}
    if "ethernet0" in value:
        import capo_panorama.types.ethernet_payload

        out["Ethernet0"] = capo_panorama.types.ethernet_payload.serialize_json(
            value["ethernet0"]
        )
    if "ethernet1" in value:
        import capo_panorama.types.ethernet_payload

        out["Ethernet1"] = capo_panorama.types.ethernet_payload.serialize_json(
            value["ethernet1"]
        )
    if "ntp" in value:
        import capo_panorama.types.ntp_payload

        out["Ntp"] = capo_panorama.types.ntp_payload.serialize_json(value["ntp"])
    return out


def deserialize_json(data: dict) -> NetworkPayload:
    out: NetworkPayload = {}  # type: ignore[typeddict-item]
    if "Ethernet0" in data:
        import capo_panorama.types.ethernet_payload

        out["ethernet0"] = capo_panorama.types.ethernet_payload.deserialize_json(
            data["Ethernet0"]
        )
    if "Ethernet1" in data:
        import capo_panorama.types.ethernet_payload

        out["ethernet1"] = capo_panorama.types.ethernet_payload.deserialize_json(
            data["Ethernet1"]
        )
    if "Ntp" in data:
        import capo_panorama.types.ntp_payload

        out["ntp"] = capo_panorama.types.ntp_payload.deserialize_json(data["Ntp"])
    return out
