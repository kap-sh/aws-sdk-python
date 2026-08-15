"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectionTrackingSpecificationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer


class ConnectionTrackingSpecificationResponse(TypedDict, closed=True):
    tcp_established_timeout: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>Timeout (in seconds) for idle TCP connections in an established state. Min: 60 seconds. Max: 432000 seconds (5 days). Default: 350 seconds for Nitro v6 instance types (excluding P6e-GB200); 432000 seconds for all other instance types (including P6e-GB200). Recommended: Less than 432000 seconds.</p>"""
    udp_stream_timeout: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>Timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction. Min: 60 seconds. Max: 180 seconds (3 minutes). Default: 180 seconds.</p>"""
    udp_timeout: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>Timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction. Min: 30 seconds. Max: 60 seconds. Default: 30 seconds.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ConnectionTrackingSpecificationResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "tcp_established_timeout" in value:
        pairs.append(
            (
                f"{key_prefix}TcpEstablishedTimeout",
                str(value["tcp_established_timeout"]),
            )
        )
    if "udp_stream_timeout" in value:
        pairs.append(
            (f"{key_prefix}UdpStreamTimeout", str(value["udp_stream_timeout"]))
        )
    if "udp_timeout" in value:
        pairs.append((f"{key_prefix}UdpTimeout", str(value["udp_timeout"])))


def deserialize_ec2_query(el: Element) -> ConnectionTrackingSpecificationResponse:
    out: ConnectionTrackingSpecificationResponse = {}  # type: ignore[typeddict-item]
    child_tcp_established_timeout = el.find("tcpEstablishedTimeout")
    if child_tcp_established_timeout is not None:
        out["tcp_established_timeout"] = int(child_tcp_established_timeout.text or "")
    child_udp_stream_timeout = el.find("udpStreamTimeout")
    if child_udp_stream_timeout is not None:
        out["udp_stream_timeout"] = int(child_udp_stream_timeout.text or "")
    child_udp_timeout = el.find("udpTimeout")
    if child_udp_timeout is not None:
        out["udp_timeout"] = int(child_udp_timeout.text or "")
    return out
