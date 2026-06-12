"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ImportFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.import_failure_list_item

ImportFailureList: TypeAlias = list[
    "aws_sdk_cloudtrail.types.import_failure_list_item.ImportFailureListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportFailureList) -> list:
    import aws_sdk_cloudtrail.types.import_failure_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudtrail.types.import_failure_list_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImportFailureList:
    import aws_sdk_cloudtrail.types.import_failure_list_item

    out: ImportFailureList = []
    for item in data:
        out.append(
            aws_sdk_cloudtrail.types.import_failure_list_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
