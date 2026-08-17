"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationExecutionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.association_execution

AssociationExecutionsList: TypeAlias = list[
    "capo_ssm.types.association_execution.AssociationExecution"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationExecutionsList) -> list:
    import capo_ssm.types.association_execution

    out: list = []
    for item in value:
        out.append(capo_ssm.types.association_execution.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AssociationExecutionsList:
    import capo_ssm.types.association_execution

    out: AssociationExecutionsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.association_execution.deserialize_aws_json_1_1(item))
    return out
