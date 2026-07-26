"""Generated from Smithy shape ``com.amazonaws.odb#PeeredCidrList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.peered_cidr

PeeredCidrList: TypeAlias = list["capo_odb.types.peered_cidr.PeeredCidr"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PeeredCidrList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> PeeredCidrList:
    return list(data)
