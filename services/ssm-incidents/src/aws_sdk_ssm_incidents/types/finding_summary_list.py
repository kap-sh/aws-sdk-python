"""Generated from Smithy shape ``com.amazonaws.ssmincidents#FindingSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.finding_summary

FindingSummaryList: TypeAlias = list[
    "aws_sdk_ssm_incidents.types.finding_summary.FindingSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingSummaryList) -> list:
    import aws_sdk_ssm_incidents.types.finding_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_incidents.types.finding_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingSummaryList:
    import aws_sdk_ssm_incidents.types.finding_summary

    out: FindingSummaryList = []
    for item in data:
        out.append(aws_sdk_ssm_incidents.types.finding_summary.deserialize_json(item))
    return out
