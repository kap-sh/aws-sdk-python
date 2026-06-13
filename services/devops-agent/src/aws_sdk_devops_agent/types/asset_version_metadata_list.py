"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetVersionMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.asset_version_metadata

AssetVersionMetadataList: TypeAlias = list[
    "aws_sdk_devops_agent.types.asset_version_metadata.AssetVersionMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetVersionMetadataList) -> list:
    import aws_sdk_devops_agent.types.asset_version_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_agent.types.asset_version_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssetVersionMetadataList:
    import aws_sdk_devops_agent.types.asset_version_metadata

    out: AssetVersionMetadataList = []
    for item in data:
        out.append(
            aws_sdk_devops_agent.types.asset_version_metadata.deserialize_json(item)
        )
    return out
