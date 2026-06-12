"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DataArtifactList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.data_artifact

DataArtifactList: TypeAlias = list["aws_sdk_marketplace_discovery.types.data_artifact.DataArtifact"]


# --- restJson1 ser/de ---
def serialize_json(value: DataArtifactList) -> list:
    import aws_sdk_marketplace_discovery.types.data_artifact
    out: list = []
    for item in value:
        out.append(aws_sdk_marketplace_discovery.types.data_artifact.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataArtifactList:
    import aws_sdk_marketplace_discovery.types.data_artifact
    out: DataArtifactList = []
    for item in data:
        out.append(aws_sdk_marketplace_discovery.types.data_artifact.deserialize_json(item))
    return out