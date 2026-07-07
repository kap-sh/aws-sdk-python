"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCoipCidrResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.coip_cidr


class CreateCoipCidrResult(TypedDict, closed=True):
    coip_cidr: NotRequired["aws_sdk_ec2.types.coip_cidr.CoipCidr"]
    """<p> Information about a range of customer-owned IP addresses. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCoipCidrResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "coip_cidr" in value:
        import aws_sdk_ec2.types.coip_cidr

        aws_sdk_ec2.types.coip_cidr.serialize_ec2_query(
            value["coip_cidr"], pairs, f"{prefix}.CoipCidr"
        )


def deserialize_ec2_query(el: Element) -> CreateCoipCidrResult:
    out: CreateCoipCidrResult = {}  # type: ignore[typeddict-item]
    child_coip_cidr = el.find("CoipCidr")
    if child_coip_cidr is not None:
        import aws_sdk_ec2.types.coip_cidr

        out["coip_cidr"] = aws_sdk_ec2.types.coip_cidr.deserialize_ec2_query(
            child_coip_cidr
        )
    return out
