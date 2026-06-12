"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableReplicaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_replica

AwsDynamoDbTableReplicaList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_dynamo_db_table_replica.AwsDynamoDbTableReplica"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableReplicaList) -> list:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_replica

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_dynamo_db_table_replica.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsDynamoDbTableReplicaList:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_replica

    out: AwsDynamoDbTableReplicaList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_dynamo_db_table_replica.deserialize_json(item)
        )
    return out
