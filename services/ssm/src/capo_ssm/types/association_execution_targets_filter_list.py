"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationExecutionTargetsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.association_execution_targets_filter

AssociationExecutionTargetsFilterList: TypeAlias = list[
    "capo_ssm.types.association_execution_targets_filter.AssociationExecutionTargetsFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationExecutionTargetsFilterList) -> list:
    import capo_ssm.types.association_execution_targets_filter

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.association_execution_targets_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssociationExecutionTargetsFilterList:
    import capo_ssm.types.association_execution_targets_filter

    out: AssociationExecutionTargetsFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ssm.types.association_execution_targets_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
