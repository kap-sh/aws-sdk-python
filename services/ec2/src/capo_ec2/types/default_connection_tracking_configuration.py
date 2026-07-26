"""Generated from Smithy shape ``com.amazonaws.ec2#DefaultConnectionTrackingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.default_tcp_established_timeout
    import capo_ec2.types.default_udp_stream_timeout
    import capo_ec2.types.default_udp_timeout


class DefaultConnectionTrackingConfiguration(TypedDict, closed=True):
    default_tcp_established_timeout: NotRequired[
        "capo_ec2.types.default_tcp_established_timeout.DefaultTcpEstablishedTimeout"
    ]
    """<p>Default timeout (in seconds) for idle TCP connections in an established state.</p>"""
    default_udp_timeout: NotRequired[
        "capo_ec2.types.default_udp_timeout.DefaultUdpTimeout"
    ]
    """<p>Default timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction.</p>"""
    default_udp_stream_timeout: NotRequired[
        "capo_ec2.types.default_udp_stream_timeout.DefaultUdpStreamTimeout"
    ]
    """<p>Default timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DefaultConnectionTrackingConfiguration,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "default_tcp_established_timeout" in value:
        pairs.append(
            (
                f"{prefix}.DefaultTcpEstablishedTimeout",
                str(value["default_tcp_established_timeout"]),
            )
        )
    if "default_udp_timeout" in value:
        pairs.append((f"{prefix}.DefaultUdpTimeout", str(value["default_udp_timeout"])))
    if "default_udp_stream_timeout" in value:
        pairs.append(
            (
                f"{prefix}.DefaultUdpStreamTimeout",
                str(value["default_udp_stream_timeout"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DefaultConnectionTrackingConfiguration:
    out: DefaultConnectionTrackingConfiguration = {}  # type: ignore[typeddict-item]
    child_default_tcp_established_timeout = el.find("DefaultTcpEstablishedTimeout")
    if child_default_tcp_established_timeout is not None:
        out["default_tcp_established_timeout"] = int(
            child_default_tcp_established_timeout.text or ""
        )
    child_default_udp_timeout = el.find("DefaultUdpTimeout")
    if child_default_udp_timeout is not None:
        out["default_udp_timeout"] = int(child_default_udp_timeout.text or "")
    child_default_udp_stream_timeout = el.find("DefaultUdpStreamTimeout")
    if child_default_udp_stream_timeout is not None:
        out["default_udp_stream_timeout"] = int(
            child_default_udp_stream_timeout.text or ""
        )
    return out
