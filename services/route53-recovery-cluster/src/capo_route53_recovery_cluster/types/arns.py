"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#Arns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.arn

Arns: TypeAlias = list["capo_route53_recovery_cluster.types.arn.Arn"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Arns) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Arns:
    return list(data)
