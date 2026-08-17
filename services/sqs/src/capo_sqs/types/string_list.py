"""Generated from Smithy shape ``com.amazonaws.sqs#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sqs.types.string

StringList: TypeAlias = list["capo_sqs.types.string.String"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StringList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> StringList:
    return [item for item in data if item is not None]
