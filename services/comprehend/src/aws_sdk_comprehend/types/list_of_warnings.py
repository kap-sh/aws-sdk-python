"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfWarnings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.warnings_list_item

ListOfWarnings: TypeAlias = list[
    "aws_sdk_comprehend.types.warnings_list_item.WarningsListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfWarnings) -> list:
    import aws_sdk_comprehend.types.warnings_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.warnings_list_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfWarnings:
    import aws_sdk_comprehend.types.warnings_list_item

    out: ListOfWarnings = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.warnings_list_item.deserialize_aws_json_1_1(item)
        )
    return out
