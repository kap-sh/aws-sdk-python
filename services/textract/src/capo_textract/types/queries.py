"""Generated from Smithy shape ``com.amazonaws.textract#Queries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.query

Queries: TypeAlias = list["capo_textract.types.query.Query"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Queries) -> list:
    import capo_textract.types.query

    out: list = []
    for item in value:
        out.append(capo_textract.types.query.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Queries:
    import capo_textract.types.query

    out: Queries = []
    for item in data:
        out.append(capo_textract.types.query.deserialize_aws_json_1_1(item))
    return out
