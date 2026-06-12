"""Generated from Smithy shape ``com.amazonaws.kendra#RetrieveResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.retrieve_result_item

RetrieveResultItemList: TypeAlias = list[
    "aws_sdk_kendra.types.retrieve_result_item.RetrieveResultItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetrieveResultItemList) -> list:
    import aws_sdk_kendra.types.retrieve_result_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.retrieve_result_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RetrieveResultItemList:
    import aws_sdk_kendra.types.retrieve_result_item

    out: RetrieveResultItemList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.retrieve_result_item.deserialize_aws_json_1_1(item)
        )
    return out
