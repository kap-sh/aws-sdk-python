"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.replication_rule

ReplicationRuleList: TypeAlias = list[
    "aws_sdk_ecr.types.replication_rule.ReplicationRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationRuleList) -> list:
    import aws_sdk_ecr.types.replication_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_ecr.types.replication_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationRuleList:
    import aws_sdk_ecr.types.replication_rule

    out: ReplicationRuleList = []
    for item in data:
        out.append(aws_sdk_ecr.types.replication_rule.deserialize_aws_json_1_1(item))
    return out
