"""Generated from Smithy shape ``com.amazonaws.kendra#QueryTextList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.query_text

QueryTextList: TypeAlias = list["aws_sdk_kendra.types.query_text.QueryText"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryTextList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> QueryTextList:
    return list(data)
