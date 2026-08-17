"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ReplicationStatusListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_secrets_manager.types.replication_status_type

ReplicationStatusListType: TypeAlias = list[
    "capo_secrets_manager.types.replication_status_type.ReplicationStatusType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationStatusListType) -> list:
    import capo_secrets_manager.types.replication_status_type

    out: list = []
    for item in value:
        out.append(
            capo_secrets_manager.types.replication_status_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationStatusListType:
    import capo_secrets_manager.types.replication_status_type

    out: ReplicationStatusListType = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_secrets_manager.types.replication_status_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
