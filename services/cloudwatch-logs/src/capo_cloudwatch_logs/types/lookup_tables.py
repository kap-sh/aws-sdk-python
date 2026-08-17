"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LookupTables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.lookup_table

LookupTables: TypeAlias = list["capo_cloudwatch_logs.types.lookup_table.LookupTable"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LookupTables) -> list:
    import capo_cloudwatch_logs.types.lookup_table

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_logs.types.lookup_table.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LookupTables:
    import capo_cloudwatch_logs.types.lookup_table

    out: LookupTables = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch_logs.types.lookup_table.deserialize_aws_json_1_1(item)
        )
    return out
