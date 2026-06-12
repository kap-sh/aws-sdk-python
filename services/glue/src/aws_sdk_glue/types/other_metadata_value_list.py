"""Generated from Smithy shape ``com.amazonaws.glue#OtherMetadataValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.other_metadata_value_list_item

OtherMetadataValueList: TypeAlias = list[
    "aws_sdk_glue.types.other_metadata_value_list_item.OtherMetadataValueListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OtherMetadataValueList) -> list:
    import aws_sdk_glue.types.other_metadata_value_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.other_metadata_value_list_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OtherMetadataValueList:
    import aws_sdk_glue.types.other_metadata_value_list_item

    out: OtherMetadataValueList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.other_metadata_value_list_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
