"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#CheckSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.check_summary

CheckSummaryList: TypeAlias = list[
    "aws_sdk_trustedadvisor.types.check_summary.CheckSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CheckSummaryList) -> list:
    import aws_sdk_trustedadvisor.types.check_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_trustedadvisor.types.check_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CheckSummaryList:
    import aws_sdk_trustedadvisor.types.check_summary

    out: CheckSummaryList = []
    for item in data:
        out.append(aws_sdk_trustedadvisor.types.check_summary.deserialize_json(item))
    return out
