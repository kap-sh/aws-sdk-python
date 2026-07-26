"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationExecutionTargetsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.association_execution_target

AssociationExecutionTargetsList: TypeAlias = list[
    "capo_ssm.types.association_execution_target.AssociationExecutionTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationExecutionTargetsList) -> list:
    import capo_ssm.types.association_execution_target

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.association_execution_target.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssociationExecutionTargetsList:
    import capo_ssm.types.association_execution_target

    out: AssociationExecutionTargetsList = []
    for item in data:
        out.append(
            capo_ssm.types.association_execution_target.deserialize_aws_json_1_1(item)
        )
    return out
