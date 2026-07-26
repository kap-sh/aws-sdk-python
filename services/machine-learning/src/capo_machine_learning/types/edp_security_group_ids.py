"""Generated from Smithy shape ``com.amazonaws.machinelearning#EDPSecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_machine_learning.types.edp_security_group_id

EDPSecurityGroupIds: TypeAlias = list[
    "capo_machine_learning.types.edp_security_group_id.EDPSecurityGroupId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EDPSecurityGroupIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EDPSecurityGroupIds:
    return list(data)
