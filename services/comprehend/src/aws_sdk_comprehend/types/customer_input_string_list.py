"""Generated from Smithy shape ``com.amazonaws.comprehend#CustomerInputStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.customer_input_string

CustomerInputStringList: TypeAlias = list[
    "aws_sdk_comprehend.types.customer_input_string.CustomerInputString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerInputStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CustomerInputStringList:
    return list(data)
