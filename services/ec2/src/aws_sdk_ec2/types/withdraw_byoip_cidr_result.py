"""Generated from Smithy shape ``com.amazonaws.ec2#WithdrawByoipCidrResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.byoip_cidr


class WithdrawByoipCidrResult(TypedDict):
    byoip_cidr: NotRequired["aws_sdk_ec2.types.byoip_cidr.ByoipCidr"]
    """<p>Information about the address pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: WithdrawByoipCidrResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "byoip_cidr" in value:
        import aws_sdk_ec2.types.byoip_cidr

        aws_sdk_ec2.types.byoip_cidr.serialize_ec2_query(
            value["byoip_cidr"], pairs, f"{prefix}.ByoipCidr"
        )


def deserialize_ec2_query(el: Element) -> WithdrawByoipCidrResult:
    out: WithdrawByoipCidrResult = {}  # type: ignore[typeddict-item]
    child_byoip_cidr = el.find("ByoipCidr")
    if child_byoip_cidr is not None:
        import aws_sdk_ec2.types.byoip_cidr

        out["byoip_cidr"] = aws_sdk_ec2.types.byoip_cidr.deserialize_ec2_query(
            child_byoip_cidr
        )
    return out
