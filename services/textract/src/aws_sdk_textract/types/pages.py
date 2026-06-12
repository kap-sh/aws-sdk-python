"""Generated from Smithy shape ``com.amazonaws.textract#Pages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.u_integer

Pages: TypeAlias = list["aws_sdk_textract.types.u_integer.UInteger"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Pages) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Pages:
    return list(data)
