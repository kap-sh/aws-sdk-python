"""Generated from Smithy shape ``com.amazonaws.servicecatalog#TagOptionValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.tag_option_value

TagOptionValues: TypeAlias = list[
    "capo_service_catalog.types.tag_option_value.TagOptionValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagOptionValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TagOptionValues:
    return list(data)
