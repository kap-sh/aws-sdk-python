"""Generated from Smithy shape ``com.amazonaws.ec2#PoolCidrBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class PoolCidrBlock(TypedDict, closed=True):
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR block.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PoolCidrBlock, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cidr" in value:
        pairs.append((f"{key_prefix}PoolCidrBlock", str(value["cidr"])))


def deserialize_ec2_query(el: Element) -> PoolCidrBlock:
    out: PoolCidrBlock = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("poolCidrBlock")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    return out
