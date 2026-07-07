"""Generated from Smithy shape ``com.amazonaws.securityhub#CidrBlockAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class CidrBlockAssociation(TypedDict, closed=True):
    association_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The association ID for the IPv4 CIDR block.</p>"""
    cidr_block: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The IPv4 CIDR block.</p>"""
    cidr_block_state: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Information about the state of the IPv4 CIDR block.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CidrBlockAssociation) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "cidr_block" in value:
        out["CidrBlock"] = value["cidr_block"]
    if "cidr_block_state" in value:
        out["CidrBlockState"] = value["cidr_block_state"]
    return out


def deserialize_json(data: dict) -> CidrBlockAssociation:
    out: CidrBlockAssociation = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "CidrBlock" in data:
        out["cidr_block"] = data["CidrBlock"]
    if "CidrBlockState" in data:
        out["cidr_block_state"] = data["CidrBlockState"]
    return out
