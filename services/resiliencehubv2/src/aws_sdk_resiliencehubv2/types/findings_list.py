"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#FindingsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.finding_summary

FindingsList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.finding_summary.FindingSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsList) -> list:
    import aws_sdk_resiliencehubv2.types.finding_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehubv2.types.finding_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingsList:
    import aws_sdk_resiliencehubv2.types.finding_summary

    out: FindingsList = []
    for item in data:
        out.append(aws_sdk_resiliencehubv2.types.finding_summary.deserialize_json(item))
    return out
