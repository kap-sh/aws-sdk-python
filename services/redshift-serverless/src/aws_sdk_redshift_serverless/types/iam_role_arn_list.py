"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#IamRoleArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.iam_role_arn

IamRoleArnList: TypeAlias = list[
    "aws_sdk_redshift_serverless.types.iam_role_arn.IamRoleArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IamRoleArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IamRoleArnList:
    return list(data)
