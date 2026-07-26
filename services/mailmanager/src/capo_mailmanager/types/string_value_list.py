"""Generated from Smithy shape ``com.amazonaws.mailmanager#StringValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.string_value

StringValueList: TypeAlias = list["capo_mailmanager.types.string_value.StringValue"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StringValueList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> StringValueList:
    return list(data)
