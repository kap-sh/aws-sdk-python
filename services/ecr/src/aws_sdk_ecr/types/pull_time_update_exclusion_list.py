"""Generated from Smithy shape ``com.amazonaws.ecr#PullTimeUpdateExclusionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.principal_arn

PullTimeUpdateExclusionList: TypeAlias = list[
    "aws_sdk_ecr.types.principal_arn.PrincipalArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullTimeUpdateExclusionList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PullTimeUpdateExclusionList:
    return list(data)
