"""Generated from Smithy shape ``com.amazonaws.athena#QueryStagePlanNodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.query_stage_plan_node

QueryStagePlanNodes: TypeAlias = list[
    "aws_sdk_athena.types.query_stage_plan_node.QueryStagePlanNode"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryStagePlanNodes) -> list:
    import aws_sdk_athena.types.query_stage_plan_node

    out: list = []
    for item in value:
        out.append(
            aws_sdk_athena.types.query_stage_plan_node.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> QueryStagePlanNodes:
    import aws_sdk_athena.types.query_stage_plan_node

    out: QueryStagePlanNodes = []
    for item in data:
        out.append(
            aws_sdk_athena.types.query_stage_plan_node.deserialize_aws_json_1_1(item)
        )
    return out
