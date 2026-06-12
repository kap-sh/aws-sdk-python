"""Generated from Smithy shape ``com.amazonaws.athena#QueryStages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.query_stage

QueryStages: TypeAlias = list["aws_sdk_athena.types.query_stage.QueryStage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryStages) -> list:
    import aws_sdk_athena.types.query_stage

    out: list = []
    for item in value:
        out.append(aws_sdk_athena.types.query_stage.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> QueryStages:
    import aws_sdk_athena.types.query_stage

    out: QueryStages = []
    for item in data:
        out.append(aws_sdk_athena.types.query_stage.deserialize_aws_json_1_1(item))
    return out
