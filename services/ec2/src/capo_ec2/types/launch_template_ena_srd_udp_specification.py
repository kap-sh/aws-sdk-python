"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateEnaSrdUdpSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class LaunchTemplateEnaSrdUdpSpecification(TypedDict, closed=True):
    ena_srd_udp_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether UDP traffic to and from the instance uses ENA Express. To specify this setting, you must first enable ENA Express.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateEnaSrdUdpSpecification,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ena_srd_udp_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}EnaSrdUdpEnabled",
                "true" if value["ena_srd_udp_enabled"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateEnaSrdUdpSpecification:
    out: LaunchTemplateEnaSrdUdpSpecification = {}  # type: ignore[typeddict-item]
    child_ena_srd_udp_enabled = el.find("EnaSrdUdpEnabled")
    if child_ena_srd_udp_enabled is not None:
        out["ena_srd_udp_enabled"] = (
            child_ena_srd_udp_enabled.text or ""
        ).lower() == "true"
    return out
