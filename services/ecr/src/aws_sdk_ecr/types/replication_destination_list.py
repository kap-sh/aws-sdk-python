"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationDestinationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.replication_destination

ReplicationDestinationList: TypeAlias = list[
    "aws_sdk_ecr.types.replication_destination.ReplicationDestination"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationDestinationList) -> list:
    import aws_sdk_ecr.types.replication_destination

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecr.types.replication_destination.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationDestinationList:
    import aws_sdk_ecr.types.replication_destination

    out: ReplicationDestinationList = []
    for item in data:
        out.append(
            aws_sdk_ecr.types.replication_destination.deserialize_aws_json_1_1(item)
        )
    return out
