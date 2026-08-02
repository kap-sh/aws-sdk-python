"""Generated from Smithy shape ``com.amazonaws.ec2#EnaSrdSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ena_srd_udp_specification_request


class EnaSrdSpecificationRequest(TypedDict, closed=True):
    ena_srd_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether ENA Express is enabled for the network interface when you launch an instance.</p>"""
    ena_srd_udp_specification: NotRequired[
        "capo_ec2.types.ena_srd_udp_specification_request.EnaSrdUdpSpecificationRequest"
    ]
    """<p>Contains ENA Express settings for UDP network traffic for the network interface attached to the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnaSrdSpecificationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ena_srd_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}EnaSrdEnabled",
                "true" if value["ena_srd_enabled"] else "false",
            )
        )
    if "ena_srd_udp_specification" in value:
        import capo_ec2.types.ena_srd_udp_specification_request

        capo_ec2.types.ena_srd_udp_specification_request.serialize_ec2_query(
            value["ena_srd_udp_specification"],
            pairs,
            f"{key_prefix}EnaSrdUdpSpecification",
        )


def deserialize_ec2_query(el: Element) -> EnaSrdSpecificationRequest:
    out: EnaSrdSpecificationRequest = {}  # type: ignore[typeddict-item]
    child_ena_srd_enabled = el.find("EnaSrdEnabled")
    if child_ena_srd_enabled is not None:
        out["ena_srd_enabled"] = (child_ena_srd_enabled.text or "").lower() == "true"
    child_ena_srd_udp_specification = el.find("EnaSrdUdpSpecification")
    if child_ena_srd_udp_specification is not None:
        import capo_ec2.types.ena_srd_udp_specification_request

        out["ena_srd_udp_specification"] = (
            capo_ec2.types.ena_srd_udp_specification_request.deserialize_ec2_query(
                child_ena_srd_udp_specification
            )
        )
    return out
