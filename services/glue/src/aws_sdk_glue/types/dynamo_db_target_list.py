"""Generated from Smithy shape ``com.amazonaws.glue#DynamoDBTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.dynamo_db_target

DynamoDBTargetList: TypeAlias = list[
    "aws_sdk_glue.types.dynamo_db_target.DynamoDBTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DynamoDBTargetList) -> list:
    import aws_sdk_glue.types.dynamo_db_target

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.dynamo_db_target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DynamoDBTargetList:
    import aws_sdk_glue.types.dynamo_db_target

    out: DynamoDBTargetList = []
    for item in data:
        out.append(aws_sdk_glue.types.dynamo_db_target.deserialize_aws_json_1_1(item))
    return out
