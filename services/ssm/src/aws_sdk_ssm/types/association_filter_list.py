"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_filter

AssociationFilterList: TypeAlias = list[
    "aws_sdk_ssm.types.association_filter.AssociationFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationFilterList) -> list:
    import aws_sdk_ssm.types.association_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.association_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AssociationFilterList:
    import aws_sdk_ssm.types.association_filter

    out: AssociationFilterList = []
    for item in data:
        out.append(aws_sdk_ssm.types.association_filter.deserialize_aws_json_1_1(item))
    return out
