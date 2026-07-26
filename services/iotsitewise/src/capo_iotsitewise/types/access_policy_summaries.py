"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AccessPolicySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.access_policy_summary

AccessPolicySummaries: TypeAlias = list[
    "capo_iotsitewise.types.access_policy_summary.AccessPolicySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessPolicySummaries) -> list:
    import capo_iotsitewise.types.access_policy_summary

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.access_policy_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessPolicySummaries:
    import capo_iotsitewise.types.access_policy_summary

    out: AccessPolicySummaries = []
    for item in data:
        out.append(capo_iotsitewise.types.access_policy_summary.deserialize_json(item))
    return out
