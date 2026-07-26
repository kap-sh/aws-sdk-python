"""Generated from Smithy shape ``com.amazonaws.b2bi#PartnershipCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_b2bi.types.capability_id

PartnershipCapabilities: TypeAlias = list["capo_b2bi.types.capability_id.CapabilityId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartnershipCapabilities) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> PartnershipCapabilities:
    return list(data)
