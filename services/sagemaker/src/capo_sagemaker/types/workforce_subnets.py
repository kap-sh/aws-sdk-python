"""Generated from Smithy shape ``com.amazonaws.sagemaker#WorkforceSubnets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.workforce_subnet_id

WorkforceSubnets: TypeAlias = list[
    "capo_sagemaker.types.workforce_subnet_id.WorkforceSubnetId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkforceSubnets) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> WorkforceSubnets:
    return list(data)
