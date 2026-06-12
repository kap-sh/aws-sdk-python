"""Generated from Smithy shape ``com.amazonaws.codeartifact#AssetSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.asset_summary

AssetSummaryList: TypeAlias = list[
    "aws_sdk_codeartifact.types.asset_summary.AssetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetSummaryList) -> list:
    import aws_sdk_codeartifact.types.asset_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_codeartifact.types.asset_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetSummaryList:
    import aws_sdk_codeartifact.types.asset_summary

    out: AssetSummaryList = []
    for item in data:
        out.append(aws_sdk_codeartifact.types.asset_summary.deserialize_json(item))
    return out
