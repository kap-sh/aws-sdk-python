"""Generated from Smithy shape ``com.amazonaws.securityagent#MembershipSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.membership_summary

MembershipSummaryList: TypeAlias = list[
    "capo_securityagent.types.membership_summary.MembershipSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MembershipSummaryList) -> list:
    import capo_securityagent.types.membership_summary

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.membership_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MembershipSummaryList:
    import capo_securityagent.types.membership_summary

    out: MembershipSummaryList = []
    for item in data:
        out.append(capo_securityagent.types.membership_summary.deserialize_json(item))
    return out
