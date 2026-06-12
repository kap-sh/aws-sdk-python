"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationExecutionFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_execution_filter

AssociationExecutionFilterList: TypeAlias = list[
    "aws_sdk_ssm.types.association_execution_filter.AssociationExecutionFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationExecutionFilterList) -> list:
    import aws_sdk_ssm.types.association_execution_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.association_execution_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssociationExecutionFilterList:
    import aws_sdk_ssm.types.association_execution_filter

    out: AssociationExecutionFilterList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.association_execution_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
