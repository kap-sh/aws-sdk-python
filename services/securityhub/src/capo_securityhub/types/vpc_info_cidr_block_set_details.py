"""Generated from Smithy shape ``com.amazonaws.securityhub#VpcInfoCidrBlockSetDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class VpcInfoCidrBlockSetDetails(TypedDict, closed=True):
    cidr_block: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The IPv4 CIDR block for the VPC. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcInfoCidrBlockSetDetails) -> dict:
    out: dict = {}
    if "cidr_block" in value:
        out["CidrBlock"] = value["cidr_block"]
    return out


def deserialize_json(data: dict) -> VpcInfoCidrBlockSetDetails:
    out: VpcInfoCidrBlockSetDetails = {}  # type: ignore[typeddict-item]
    if "CidrBlock" in data:
        out["cidr_block"] = data["CidrBlock"]
    return out
