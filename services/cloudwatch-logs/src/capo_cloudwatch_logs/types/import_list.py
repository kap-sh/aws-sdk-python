"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ImportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.import_

ImportList: TypeAlias = list["capo_cloudwatch_logs.types.import_.Import"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportList) -> list:
    import capo_cloudwatch_logs.types.import_

    out: list = []
    for item in value:
        out.append(capo_cloudwatch_logs.types.import_.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImportList:
    import capo_cloudwatch_logs.types.import_

    out: ImportList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudwatch_logs.types.import_.deserialize_aws_json_1_1(item))
    return out
