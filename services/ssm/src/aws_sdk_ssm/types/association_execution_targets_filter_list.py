"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationExecutionTargetsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_execution_targets_filter

AssociationExecutionTargetsFilterList: TypeAlias = list[
    "aws_sdk_ssm.types.association_execution_targets_filter.AssociationExecutionTargetsFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationExecutionTargetsFilterList) -> list:
    import aws_sdk_ssm.types.association_execution_targets_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.association_execution_targets_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssociationExecutionTargetsFilterList:
    import aws_sdk_ssm.types.association_execution_targets_filter

    out: AssociationExecutionTargetsFilterList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.association_execution_targets_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
