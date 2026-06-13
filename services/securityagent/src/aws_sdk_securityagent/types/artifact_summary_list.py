"""Generated from Smithy shape ``com.amazonaws.securityagent#ArtifactSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.artifact_summary

ArtifactSummaryList: TypeAlias = list[
    "aws_sdk_securityagent.types.artifact_summary.ArtifactSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactSummaryList) -> list:
    import aws_sdk_securityagent.types.artifact_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_securityagent.types.artifact_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ArtifactSummaryList:
    import aws_sdk_securityagent.types.artifact_summary

    out: ArtifactSummaryList = []
    for item in data:
        out.append(aws_sdk_securityagent.types.artifact_summary.deserialize_json(item))
    return out
