"""Generated from Smithy shape ``com.amazonaws.cloudtrail#AdvancedFieldSelectors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.advanced_field_selector

AdvancedFieldSelectors: TypeAlias = list[
    "aws_sdk_cloudtrail.types.advanced_field_selector.AdvancedFieldSelector"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdvancedFieldSelectors) -> list:
    import aws_sdk_cloudtrail.types.advanced_field_selector

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudtrail.types.advanced_field_selector.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AdvancedFieldSelectors:
    import aws_sdk_cloudtrail.types.advanced_field_selector

    out: AdvancedFieldSelectors = []
    for item in data:
        out.append(
            aws_sdk_cloudtrail.types.advanced_field_selector.deserialize_aws_json_1_1(
                item
            )
        )
    return out
