"""Generated from Smithy shape ``com.amazonaws.securityagent#ArtifactMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.artifact_metadata_item

ArtifactMetadataList: TypeAlias = list[
    "aws_sdk_securityagent.types.artifact_metadata_item.ArtifactMetadataItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactMetadataList) -> list:
    import aws_sdk_securityagent.types.artifact_metadata_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityagent.types.artifact_metadata_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ArtifactMetadataList:
    import aws_sdk_securityagent.types.artifact_metadata_item

    out: ArtifactMetadataList = []
    for item in data:
        out.append(
            aws_sdk_securityagent.types.artifact_metadata_item.deserialize_json(item)
        )
    return out
