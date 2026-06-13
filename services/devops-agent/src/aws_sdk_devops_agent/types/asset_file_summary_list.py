"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetFileSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.asset_file_summary

AssetFileSummaryList: TypeAlias = list[
    "aws_sdk_devops_agent.types.asset_file_summary.AssetFileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetFileSummaryList) -> list:
    import aws_sdk_devops_agent.types.asset_file_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_agent.types.asset_file_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetFileSummaryList:
    import aws_sdk_devops_agent.types.asset_file_summary

    out: AssetFileSummaryList = []
    for item in data:
        out.append(aws_sdk_devops_agent.types.asset_file_summary.deserialize_json(item))
    return out
