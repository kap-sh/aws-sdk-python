"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeActivationsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.describe_activations_filter

DescribeActivationsFilterList: TypeAlias = list[
    "aws_sdk_ssm.types.describe_activations_filter.DescribeActivationsFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeActivationsFilterList) -> list:
    import aws_sdk_ssm.types.describe_activations_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.describe_activations_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DescribeActivationsFilterList:
    import aws_sdk_ssm.types.describe_activations_filter

    out: DescribeActivationsFilterList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.describe_activations_filter.deserialize_aws_json_1_1(item)
        )
    return out
