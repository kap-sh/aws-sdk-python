"""Generated from Smithy shape ``com.amazonaws.ec2#PoolCidrBlock``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class PoolCidrBlock(TypedDict):
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR block.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PoolCidrBlock, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cidr" in value:
        pairs.append((f"{prefix}.PoolCidrBlock", str(value["cidr"])))


def deserialize_ec2_query(el: Element) -> PoolCidrBlock:
    out: PoolCidrBlock = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("PoolCidrBlock")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    return out
