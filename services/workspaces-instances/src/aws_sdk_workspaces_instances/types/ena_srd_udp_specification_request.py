"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#EnaSrdUdpSpecificationRequest``."""

from typing import TypedDict

from typing_extensions import NotRequired


class EnaSrdUdpSpecificationRequest(TypedDict):
    ena_srd_udp_enabled: NotRequired["bool"]
    """<p>Enables or disables ENA SRD for UDP traffic.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnaSrdUdpSpecificationRequest) -> dict:
    out: dict = {}
    if "ena_srd_udp_enabled" in value:
        out["EnaSrdUdpEnabled"] = value["ena_srd_udp_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EnaSrdUdpSpecificationRequest:
    out: EnaSrdUdpSpecificationRequest = {}  # type: ignore[typeddict-item]
    if "EnaSrdUdpEnabled" in data:
        out["ena_srd_udp_enabled"] = data["EnaSrdUdpEnabled"]
    return out
