"""Generated from Smithy shape ``com.amazonaws.transfer#ListedExecutions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transfer.types.listed_execution

ListedExecutions: TypeAlias = list[
    "aws_sdk_transfer.types.listed_execution.ListedExecution"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedExecutions) -> list:
    import aws_sdk_transfer.types.listed_execution

    out: list = []
    for item in value:
        out.append(aws_sdk_transfer.types.listed_execution.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListedExecutions:
    import aws_sdk_transfer.types.listed_execution

    out: ListedExecutions = []
    for item in data:
        out.append(
            aws_sdk_transfer.types.listed_execution.deserialize_aws_json_1_1(item)
        )
    return out
