"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#CheckSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_trustedadvisor.types.check_summary

CheckSummaryList: TypeAlias = list[
    "capo_trustedadvisor.types.check_summary.CheckSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CheckSummaryList) -> list:
    import capo_trustedadvisor.types.check_summary

    out: list = []
    for item in value:
        out.append(capo_trustedadvisor.types.check_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CheckSummaryList:
    import capo_trustedadvisor.types.check_summary

    out: CheckSummaryList = []
    for item in data:
        out.append(capo_trustedadvisor.types.check_summary.deserialize_json(item))
    return out
