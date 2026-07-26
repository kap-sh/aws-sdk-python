"""Generated from Smithy shape ``com.amazonaws.securityagent#ArtifactSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.artifact_summary

ArtifactSummaryList: TypeAlias = list[
    "capo_securityagent.types.artifact_summary.ArtifactSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactSummaryList) -> list:
    import capo_securityagent.types.artifact_summary

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.artifact_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ArtifactSummaryList:
    import capo_securityagent.types.artifact_summary

    out: ArtifactSummaryList = []
    for item in data:
        out.append(capo_securityagent.types.artifact_summary.deserialize_json(item))
    return out
