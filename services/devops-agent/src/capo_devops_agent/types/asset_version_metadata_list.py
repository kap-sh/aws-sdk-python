"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetVersionMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.asset_version_metadata

AssetVersionMetadataList: TypeAlias = list[
    "capo_devops_agent.types.asset_version_metadata.AssetVersionMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetVersionMetadataList) -> list:
    import capo_devops_agent.types.asset_version_metadata

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.asset_version_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetVersionMetadataList:
    import capo_devops_agent.types.asset_version_metadata

    out: AssetVersionMetadataList = []
    for item in data:
        out.append(
            capo_devops_agent.types.asset_version_metadata.deserialize_json(item)
        )
    return out
