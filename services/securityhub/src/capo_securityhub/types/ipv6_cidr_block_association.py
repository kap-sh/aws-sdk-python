"""Generated from Smithy shape ``com.amazonaws.securityhub#Ipv6CidrBlockAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class Ipv6CidrBlockAssociation(TypedDict, closed=True):
    association_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The association ID for the IPv6 CIDR block.</p>"""
    ipv6_cidr_block: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The IPv6 CIDR block.</p>"""
    cidr_block_state: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Information about the state of the CIDR block. Valid values are as follows:</p> <ul> <li> <p> <code>associating</code> </p> </li> <li> <p> <code>associated</code> </p> </li> <li> <p> <code>disassociating</code> </p> </li> <li> <p> <code>disassociated</code> </p> </li> <li> <p> <code>failed</code> </p> </li> <li> <p> <code>failing</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ipv6CidrBlockAssociation) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "ipv6_cidr_block" in value:
        out["Ipv6CidrBlock"] = value["ipv6_cidr_block"]
    if "cidr_block_state" in value:
        out["CidrBlockState"] = value["cidr_block_state"]
    return out


def deserialize_json(data: dict) -> Ipv6CidrBlockAssociation:
    out: Ipv6CidrBlockAssociation = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    if "Ipv6CidrBlock" in data:
        out["ipv6_cidr_block"] = data["Ipv6CidrBlock"]
    if "CidrBlockState" in data:
        out["cidr_block_state"] = data["CidrBlockState"]
    return out
