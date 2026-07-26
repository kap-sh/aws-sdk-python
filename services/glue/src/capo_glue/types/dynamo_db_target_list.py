"""Generated from Smithy shape ``com.amazonaws.glue#DynamoDBTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.dynamo_db_target

DynamoDBTargetList: TypeAlias = list["capo_glue.types.dynamo_db_target.DynamoDBTarget"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DynamoDBTargetList) -> list:
    import capo_glue.types.dynamo_db_target

    out: list = []
    for item in value:
        out.append(capo_glue.types.dynamo_db_target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DynamoDBTargetList:
    import capo_glue.types.dynamo_db_target

    out: DynamoDBTargetList = []
    for item in data:
        out.append(capo_glue.types.dynamo_db_target.deserialize_aws_json_1_1(item))
    return out
