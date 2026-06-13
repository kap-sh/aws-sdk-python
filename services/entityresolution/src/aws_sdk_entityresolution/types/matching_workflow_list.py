"""Generated from Smithy shape ``com.amazonaws.entityresolution#MatchingWorkflowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.matching_workflow_summary

MatchingWorkflowList: TypeAlias = list[
    "aws_sdk_entityresolution.types.matching_workflow_summary.MatchingWorkflowSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchingWorkflowList) -> list:
    import aws_sdk_entityresolution.types.matching_workflow_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.matching_workflow_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MatchingWorkflowList:
    import aws_sdk_entityresolution.types.matching_workflow_summary

    out: MatchingWorkflowList = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.matching_workflow_summary.deserialize_json(
                item
            )
        )
    return out
