"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeActivationsFilterKeys``."""

from typing import Literal, TypeAlias, cast

DescribeActivationsFilterKeys: TypeAlias = Literal[
    "ActivationIds",
    "DefaultInstanceName",
    "IamRole",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeActivationsFilterKeys) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DescribeActivationsFilterKeys:
    return cast(DescribeActivationsFilterKeys, data)
