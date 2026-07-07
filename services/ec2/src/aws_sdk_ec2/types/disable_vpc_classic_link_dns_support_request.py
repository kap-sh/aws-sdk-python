"""Generated from Smithy shape ``com.amazonaws.ec2#DisableVpcClassicLinkDnsSupportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_id


class DisableVpcClassicLinkDnsSupportRequest(TypedDict, closed=True):
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableVpcClassicLinkDnsSupportRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))


def deserialize_ec2_query(el: Element) -> DisableVpcClassicLinkDnsSupportRequest:
    out: DisableVpcClassicLinkDnsSupportRequest = {}  # type: ignore[typeddict-item]
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    return out
