"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.replication_rule

ReplicationRuleList: TypeAlias = list["capo_ecr.types.replication_rule.ReplicationRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationRuleList) -> list:
    import capo_ecr.types.replication_rule

    out: list = []
    for item in value:
        out.append(capo_ecr.types.replication_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationRuleList:
    import capo_ecr.types.replication_rule

    out: ReplicationRuleList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecr.types.replication_rule.deserialize_aws_json_1_1(item))
    return out
