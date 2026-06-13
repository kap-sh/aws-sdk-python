"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DependencySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.dependency_summary

DependencySummaryList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.dependency_summary.DependencySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DependencySummaryList) -> list:
    import aws_sdk_resiliencehubv2.types.dependency_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehubv2.types.dependency_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DependencySummaryList:
    import aws_sdk_resiliencehubv2.types.dependency_summary

    out: DependencySummaryList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehubv2.types.dependency_summary.deserialize_json(item)
        )
    return out
