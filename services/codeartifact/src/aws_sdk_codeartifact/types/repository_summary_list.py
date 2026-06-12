"""Generated from Smithy shape ``com.amazonaws.codeartifact#RepositorySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.repository_summary

RepositorySummaryList: TypeAlias = list[
    "aws_sdk_codeartifact.types.repository_summary.RepositorySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RepositorySummaryList) -> list:
    import aws_sdk_codeartifact.types.repository_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_codeartifact.types.repository_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> RepositorySummaryList:
    import aws_sdk_codeartifact.types.repository_summary

    out: RepositorySummaryList = []
    for item in data:
        out.append(aws_sdk_codeartifact.types.repository_summary.deserialize_json(item))
    return out
