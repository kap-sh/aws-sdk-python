"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteCoipCidrResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.coip_cidr


class DeleteCoipCidrResult(TypedDict, closed=True):
    coip_cidr: NotRequired["capo_ec2.types.coip_cidr.CoipCidr"]
    """<p> Information about a range of customer-owned IP addresses. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteCoipCidrResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "coip_cidr" in value:
        import capo_ec2.types.coip_cidr

        capo_ec2.types.coip_cidr.serialize_ec2_query(
            value["coip_cidr"], pairs, f"{key_prefix}CoipCidr"
        )


def deserialize_ec2_query(el: Element) -> DeleteCoipCidrResult:
    out: DeleteCoipCidrResult = {}  # type: ignore[typeddict-item]
    child_coip_cidr = el.find("coipCidr")
    if child_coip_cidr is not None:
        import capo_ec2.types.coip_cidr

        out["coip_cidr"] = capo_ec2.types.coip_cidr.deserialize_ec2_query(
            child_coip_cidr
        )
    return out
