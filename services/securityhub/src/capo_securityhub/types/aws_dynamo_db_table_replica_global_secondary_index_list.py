"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableReplicaGlobalSecondaryIndexList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_dynamo_db_table_replica_global_secondary_index

AwsDynamoDbTableReplicaGlobalSecondaryIndexList: TypeAlias = list[
    "capo_securityhub.types.aws_dynamo_db_table_replica_global_secondary_index.AwsDynamoDbTableReplicaGlobalSecondaryIndex"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableReplicaGlobalSecondaryIndexList) -> list:
    import capo_securityhub.types.aws_dynamo_db_table_replica_global_secondary_index

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_dynamo_db_table_replica_global_secondary_index.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsDynamoDbTableReplicaGlobalSecondaryIndexList:
    import capo_securityhub.types.aws_dynamo_db_table_replica_global_secondary_index

    out: AwsDynamoDbTableReplicaGlobalSecondaryIndexList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_dynamo_db_table_replica_global_secondary_index.deserialize_json(
                item
            )
        )
    return out
