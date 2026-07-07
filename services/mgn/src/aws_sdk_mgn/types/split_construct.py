"""Generated from Smithy shape ``com.amazonaws.mgn#SplitConstruct``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.cidr_block


class SplitConstruct(TypedDict, closed=True):
    cidr_block: NotRequired["aws_sdk_mgn.types.cidr_block.CidrBlock"]
    """<p>The CIDR block for the split construct.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SplitConstruct) -> dict:
    out: dict = {}
    if "cidr_block" in value:
        out["cidrBlock"] = value["cidr_block"]
    return out


def deserialize_json(data: dict) -> SplitConstruct:
    out: SplitConstruct = {}  # type: ignore[typeddict-item]
    if "cidrBlock" in data:
        out["cidr_block"] = data["cidrBlock"]
    return out
