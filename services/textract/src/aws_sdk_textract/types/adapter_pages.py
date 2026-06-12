"""Generated from Smithy shape ``com.amazonaws.textract#AdapterPages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapter_page

AdapterPages: TypeAlias = list["aws_sdk_textract.types.adapter_page.AdapterPage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdapterPages) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AdapterPages:
    return list(data)
