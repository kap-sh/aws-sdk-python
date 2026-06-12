"""Generated from Smithy shape ``com.amazonaws.glue#ListOfString``."""

from typing import TypeAlias

ListOfString: TypeAlias = list["str"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfString) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ListOfString:
    return list(data)
