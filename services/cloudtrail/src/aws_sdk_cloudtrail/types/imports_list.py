"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ImportsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.imports_list_item

ImportsList: TypeAlias = list[
    "aws_sdk_cloudtrail.types.imports_list_item.ImportsListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportsList) -> list:
    import aws_sdk_cloudtrail.types.imports_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudtrail.types.imports_list_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImportsList:
    import aws_sdk_cloudtrail.types.imports_list_item

    out: ImportsList = []
    for item in data:
        out.append(
            aws_sdk_cloudtrail.types.imports_list_item.deserialize_aws_json_1_1(item)
        )
    return out
