"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.asset

AssetList: TypeAlias = list["capo_devops_agent.types.asset.Asset"]


# --- restJson1 ser/de ---
def serialize_json(value: AssetList) -> list:
    import capo_devops_agent.types.asset

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.asset.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetList:
    import capo_devops_agent.types.asset

    out: AssetList = []
    for item in data:
        out.append(capo_devops_agent.types.asset.deserialize_json(item))
    return out
