"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GroupingIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.grouping_identifier

GroupingIdentifiers: TypeAlias = list[
    "capo_cloudwatch_logs.types.grouping_identifier.GroupingIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupingIdentifiers) -> list:
    import capo_cloudwatch_logs.types.grouping_identifier

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch_logs.types.grouping_identifier.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GroupingIdentifiers:
    import capo_cloudwatch_logs.types.grouping_identifier

    out: GroupingIdentifiers = []
    for item in data:
        out.append(
            capo_cloudwatch_logs.types.grouping_identifier.deserialize_aws_json_1_1(
                item
            )
        )
    return out
