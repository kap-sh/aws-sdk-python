"""Generated from Smithy shape ``com.amazonaws.textract#QueryPages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.query_page

QueryPages: TypeAlias = list["capo_textract.types.query_page.QueryPage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryPages) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> QueryPages:
    return list(data)
