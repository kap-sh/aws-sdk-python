"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.asset_type_summary

AssetTypeList: TypeAlias = list[
    "aws_sdk_devops_agent.types.asset_type_summary.AssetTypeSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetTypeList) -> list:
    import aws_sdk_devops_agent.types.asset_type_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_agent.types.asset_type_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetTypeList:
    import aws_sdk_devops_agent.types.asset_type_summary

    out: AssetTypeList = []
    for item in data:
        out.append(aws_sdk_devops_agent.types.asset_type_summary.deserialize_json(item))
    return out
