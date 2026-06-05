"""Generated from Smithy shape ``com.amazonaws.ec2#CidrBlock``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CidrBlock(TypedDict):
    cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR block.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CidrBlock, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cidr_block" in value:
        pairs.append((f"{prefix}.CidrBlock", str(value["cidr_block"])))


def deserialize_ec2_query(el: Element) -> CidrBlock:
    out: CidrBlock = {}  # type: ignore[typeddict-item]
    child_cidr_block = el.find("CidrBlock")
    if child_cidr_block is not None:
        out["cidr_block"] = str(child_cidr_block.text or "")
    return out
