"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.errors_list_item

ListOfErrors: TypeAlias = list[
    "aws_sdk_comprehend.types.errors_list_item.ErrorsListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfErrors) -> list:
    import aws_sdk_comprehend.types.errors_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.errors_list_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfErrors:
    import aws_sdk_comprehend.types.errors_list_item

    out: ListOfErrors = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.errors_list_item.deserialize_aws_json_1_1(item)
        )
    return out
