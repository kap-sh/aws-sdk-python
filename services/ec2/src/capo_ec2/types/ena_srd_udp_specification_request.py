"""Generated from Smithy shape ``com.amazonaws.ec2#EnaSrdUdpSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class EnaSrdUdpSpecificationRequest(TypedDict, closed=True):
    ena_srd_udp_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether UDP traffic uses ENA Express for your instance. To ensure that UDP traffic can use ENA Express when you launch an instance, you must also set <b>EnaSrdEnabled</b> in the <b>EnaSrdSpecificationRequest</b> to <code>true</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnaSrdUdpSpecificationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ena_srd_udp_enabled" in value:
        pairs.append(
            (
                f"{prefix}.EnaSrdUdpEnabled",
                "true" if value["ena_srd_udp_enabled"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> EnaSrdUdpSpecificationRequest:
    out: EnaSrdUdpSpecificationRequest = {}  # type: ignore[typeddict-item]
    child_ena_srd_udp_enabled = el.find("EnaSrdUdpEnabled")
    if child_ena_srd_udp_enabled is not None:
        out["ena_srd_udp_enabled"] = (
            child_ena_srd_udp_enabled.text or ""
        ).lower() == "true"
    return out
