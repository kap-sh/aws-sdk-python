"""Generated from Smithy shape ``com.amazonaws.proton#RepositorySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_proton.types.repository_summary

RepositorySummaryList: TypeAlias = list[
    "capo_proton.types.repository_summary.RepositorySummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySummaryList) -> list:
    import capo_proton.types.repository_summary

    out: list = []
    for item in value:
        out.append(capo_proton.types.repository_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> RepositorySummaryList:
    import capo_proton.types.repository_summary

    out: RepositorySummaryList = []
    for item in data:
        out.append(capo_proton.types.repository_summary.deserialize_aws_json_1_0(item))
    return out
