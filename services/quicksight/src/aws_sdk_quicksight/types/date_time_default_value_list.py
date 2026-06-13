"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeDefaultValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sensitive_timestamp

DateTimeDefaultValueList: TypeAlias = list[
    "aws_sdk_quicksight.types.sensitive_timestamp.SensitiveTimestamp"
]


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeDefaultValueList) -> list:
    import aws_sdk_quicksight.types.sensitive_timestamp

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.sensitive_timestamp.serialize_json(item))
    return out


def deserialize_json(data: list) -> DateTimeDefaultValueList:
    import aws_sdk_quicksight.types.sensitive_timestamp

    out: DateTimeDefaultValueList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.sensitive_timestamp.deserialize_json(item))
    return out
