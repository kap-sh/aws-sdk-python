"""Generated from Smithy shape ``com.amazonaws.kendra#QueryResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.query_result_item

QueryResultItemList: TypeAlias = list[
    "capo_kendra.types.query_result_item.QueryResultItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryResultItemList) -> list:
    import capo_kendra.types.query_result_item

    out: list = []
    for item in value:
        out.append(capo_kendra.types.query_result_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> QueryResultItemList:
    import capo_kendra.types.query_result_item

    out: QueryResultItemList = []
    for item in data:
        out.append(capo_kendra.types.query_result_item.deserialize_aws_json_1_1(item))
    return out
