"""Generated from Smithy shape ``com.amazonaws.panorama#NetworkStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_panorama.types.ethernet_status
    import aws_sdk_panorama.types.last_updated_time
    import aws_sdk_panorama.types.ntp_status


class NetworkStatus(TypedDict):
    ethernet0_status: NotRequired[
        "aws_sdk_panorama.types.ethernet_status.EthernetStatus"
    ]
    """<p>The status of Ethernet port 0.</p>"""
    ethernet1_status: NotRequired[
        "aws_sdk_panorama.types.ethernet_status.EthernetStatus"
    ]
    """<p>The status of Ethernet port 1.</p>"""
    ntp_status: NotRequired["aws_sdk_panorama.types.ntp_status.NtpStatus"]
    """<p>Details about a network time protocol (NTP) server connection.</p>"""
    last_updated_time: NotRequired[
        "aws_sdk_panorama.types.last_updated_time.LastUpdatedTime"
    ]
    """<p>When the network status changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkStatus) -> dict:
    out: dict = {}
    if "ethernet0_status" in value:
        import aws_sdk_panorama.types.ethernet_status

        out["Ethernet0Status"] = aws_sdk_panorama.types.ethernet_status.serialize_json(
            value["ethernet0_status"]
        )
    if "ethernet1_status" in value:
        import aws_sdk_panorama.types.ethernet_status

        out["Ethernet1Status"] = aws_sdk_panorama.types.ethernet_status.serialize_json(
            value["ethernet1_status"]
        )
    if "ntp_status" in value:
        import aws_sdk_panorama.types.ntp_status

        out["NtpStatus"] = aws_sdk_panorama.types.ntp_status.serialize_json(
            value["ntp_status"]
        )
    if "last_updated_time" in value:
        import aws_sdk_panorama.types.last_updated_time

        out["LastUpdatedTime"] = (
            aws_sdk_panorama.types.last_updated_time.serialize_json(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkStatus:
    out: NetworkStatus = {}  # type: ignore[typeddict-item]
    if "Ethernet0Status" in data:
        import aws_sdk_panorama.types.ethernet_status

        out["ethernet0_status"] = (
            aws_sdk_panorama.types.ethernet_status.deserialize_json(
                data["Ethernet0Status"]
            )
        )
    if "Ethernet1Status" in data:
        import aws_sdk_panorama.types.ethernet_status

        out["ethernet1_status"] = (
            aws_sdk_panorama.types.ethernet_status.deserialize_json(
                data["Ethernet1Status"]
            )
        )
    if "NtpStatus" in data:
        import aws_sdk_panorama.types.ntp_status

        out["ntp_status"] = aws_sdk_panorama.types.ntp_status.deserialize_json(
            data["NtpStatus"]
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_panorama.types.last_updated_time

        out["last_updated_time"] = (
            aws_sdk_panorama.types.last_updated_time.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    return out
