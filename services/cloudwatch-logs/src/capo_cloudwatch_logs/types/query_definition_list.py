"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.query_definition

QueryDefinitionList: TypeAlias = list[
    "capo_cloudwatch_logs.types.query_definition.QueryDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryDefinitionList) -> list:
    import capo_cloudwatch_logs.types.query_definition

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.query_definition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> QueryDefinitionList:
    import capo_cloudwatch_logs.types.query_definition

    out: QueryDefinitionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.query_definition.deserialize_aws_json_1_1(item)
        )
    return out
