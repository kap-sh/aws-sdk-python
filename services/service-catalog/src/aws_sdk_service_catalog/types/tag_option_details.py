"""Generated from Smithy shape ``com.amazonaws.servicecatalog#TagOptionDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.tag_option_detail

TagOptionDetails: TypeAlias = list[
    "aws_sdk_service_catalog.types.tag_option_detail.TagOptionDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagOptionDetails) -> list:
    import aws_sdk_service_catalog.types.tag_option_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.tag_option_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TagOptionDetails:
    import aws_sdk_service_catalog.types.tag_option_detail

    out: TagOptionDetails = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.tag_option_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
