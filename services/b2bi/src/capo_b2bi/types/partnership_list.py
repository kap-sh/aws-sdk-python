"""Generated from Smithy shape ``com.amazonaws.b2bi#PartnershipList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_b2bi.types.partnership_summary

PartnershipList: TypeAlias = list[
    "capo_b2bi.types.partnership_summary.PartnershipSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartnershipList) -> list:
    import capo_b2bi.types.partnership_summary

    out: list = []
    for item in value:
        out.append(capo_b2bi.types.partnership_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> PartnershipList:
    import capo_b2bi.types.partnership_summary

    out: PartnershipList = []
    for item in data:
        out.append(capo_b2bi.types.partnership_summary.deserialize_aws_json_1_0(item))
    return out
