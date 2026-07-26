"""Generated from Smithy shape ``com.amazonaws.mpa#PolicyVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mpa.types.policy_version_summary

PolicyVersions: TypeAlias = list[
    "capo_mpa.types.policy_version_summary.PolicyVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyVersions) -> list:
    import capo_mpa.types.policy_version_summary

    out: list = []
    for item in value:
        out.append(capo_mpa.types.policy_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PolicyVersions:
    import capo_mpa.types.policy_version_summary

    out: PolicyVersions = []
    for item in data:
        out.append(capo_mpa.types.policy_version_summary.deserialize_json(item))
    return out
