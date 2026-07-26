"""Generated from Smithy shape ``com.amazonaws.glue#MongoDBTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.mongo_db_target

MongoDBTargetList: TypeAlias = list["capo_glue.types.mongo_db_target.MongoDBTarget"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MongoDBTargetList) -> list:
    import capo_glue.types.mongo_db_target

    out: list = []
    for item in value:
        out.append(capo_glue.types.mongo_db_target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MongoDBTargetList:
    import capo_glue.types.mongo_db_target

    out: MongoDBTargetList = []
    for item in data:
        out.append(capo_glue.types.mongo_db_target.deserialize_aws_json_1_1(item))
    return out
