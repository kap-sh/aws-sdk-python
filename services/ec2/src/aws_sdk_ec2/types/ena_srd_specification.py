"""Generated from Smithy shape ``com.amazonaws.ec2#EnaSrdSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ena_srd_udp_specification


class EnaSrdSpecification(TypedDict):
    ena_srd_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether ENA Express is enabled for the network interface.</p>"""
    ena_srd_udp_specification: NotRequired[
        "aws_sdk_ec2.types.ena_srd_udp_specification.EnaSrdUdpSpecification"
    ]
    """<p>Configures ENA Express for UDP network traffic.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnaSrdSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ena_srd_enabled" in value:
        pairs.append(
            (f"{prefix}.EnaSrdEnabled", "true" if value["ena_srd_enabled"] else "false")
        )
    if "ena_srd_udp_specification" in value:
        import aws_sdk_ec2.types.ena_srd_udp_specification

        aws_sdk_ec2.types.ena_srd_udp_specification.serialize_ec2_query(
            value["ena_srd_udp_specification"],
            pairs,
            f"{prefix}.EnaSrdUdpSpecification",
        )


def deserialize_ec2_query(el: Element) -> EnaSrdSpecification:
    out: EnaSrdSpecification = {}  # type: ignore[typeddict-item]
    child_ena_srd_enabled = el.find("EnaSrdEnabled")
    if child_ena_srd_enabled is not None:
        out["ena_srd_enabled"] = (child_ena_srd_enabled.text or "").lower() == "true"
    child_ena_srd_udp_specification = el.find("EnaSrdUdpSpecification")
    if child_ena_srd_udp_specification is not None:
        import aws_sdk_ec2.types.ena_srd_udp_specification

        out["ena_srd_udp_specification"] = (
            aws_sdk_ec2.types.ena_srd_udp_specification.deserialize_ec2_query(
                child_ena_srd_udp_specification
            )
        )
    return out
