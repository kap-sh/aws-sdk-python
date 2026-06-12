"""Generated from Smithy shape ``com.amazonaws.glue#MongoDBTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.mongo_db_target

MongoDBTargetList: TypeAlias = list["aws_sdk_glue.types.mongo_db_target.MongoDBTarget"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MongoDBTargetList) -> list:
    import aws_sdk_glue.types.mongo_db_target

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.mongo_db_target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MongoDBTargetList:
    import aws_sdk_glue.types.mongo_db_target

    out: MongoDBTargetList = []
    for item in data:
        out.append(aws_sdk_glue.types.mongo_db_target.deserialize_aws_json_1_1(item))
    return out
