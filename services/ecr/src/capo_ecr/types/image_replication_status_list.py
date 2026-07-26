"""Generated from Smithy shape ``com.amazonaws.ecr#ImageReplicationStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.image_replication_status

ImageReplicationStatusList: TypeAlias = list[
    "capo_ecr.types.image_replication_status.ImageReplicationStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageReplicationStatusList) -> list:
    import capo_ecr.types.image_replication_status

    out: list = []
    for item in value:
        out.append(capo_ecr.types.image_replication_status.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageReplicationStatusList:
    import capo_ecr.types.image_replication_status

    out: ImageReplicationStatusList = []
    for item in data:
        out.append(
            capo_ecr.types.image_replication_status.deserialize_aws_json_1_1(item)
        )
    return out
