"""Generated from Smithy shape ``com.amazonaws.securityagent#TargetDomainSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.target_domain_summary

TargetDomainSummaryList: TypeAlias = list[
    "capo_securityagent.types.target_domain_summary.TargetDomainSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetDomainSummaryList) -> list:
    import capo_securityagent.types.target_domain_summary

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.target_domain_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TargetDomainSummaryList:
    import capo_securityagent.types.target_domain_summary

    out: TargetDomainSummaryList = []
    for item in data:
        out.append(
            capo_securityagent.types.target_domain_summary.deserialize_json(item)
        )
    return out
