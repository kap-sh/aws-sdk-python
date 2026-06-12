"""Generated from Smithy shape ``com.amazonaws.outposts#CIDRList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.cidr

CIDRList: TypeAlias = list["aws_sdk_outposts.types.cidr.CIDR"]


# --- restJson1 ser/de ---
def serialize_json(value: CIDRList) -> list:
    return list(value)


def deserialize_json(data: list) -> CIDRList:
    return list(data)
