"""Generated from Smithy shape ``com.amazonaws.connecthealth#DomainSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connecthealth.types.domain_summary

DomainSummaryList: TypeAlias = list[
    "capo_connecthealth.types.domain_summary.DomainSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainSummaryList) -> list:
    import capo_connecthealth.types.domain_summary

    out: list = []
    for item in value:
        out.append(capo_connecthealth.types.domain_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainSummaryList:
    import capo_connecthealth.types.domain_summary

    out: DomainSummaryList = []
    for item in data:
        out.append(capo_connecthealth.types.domain_summary.deserialize_json(item))
    return out
