"""Generated from Smithy shape ``com.amazonaws.b2bi#CapabilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_b2bi.types.capability_summary

CapabilityList: TypeAlias = list["capo_b2bi.types.capability_summary.CapabilitySummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapabilityList) -> list:
    import capo_b2bi.types.capability_summary

    out: list = []
    for item in value:
        out.append(capo_b2bi.types.capability_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> CapabilityList:
    import capo_b2bi.types.capability_summary

    out: CapabilityList = []
    for item in data:
        out.append(capo_b2bi.types.capability_summary.deserialize_aws_json_1_0(item))
    return out
