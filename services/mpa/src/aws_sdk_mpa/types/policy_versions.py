"""Generated from Smithy shape ``com.amazonaws.mpa#PolicyVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mpa.types.policy_version_summary

PolicyVersions: TypeAlias = list[
    "aws_sdk_mpa.types.policy_version_summary.PolicyVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyVersions) -> list:
    import aws_sdk_mpa.types.policy_version_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_mpa.types.policy_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PolicyVersions:
    import aws_sdk_mpa.types.policy_version_summary

    out: PolicyVersions = []
    for item in data:
        out.append(aws_sdk_mpa.types.policy_version_summary.deserialize_json(item))
    return out
