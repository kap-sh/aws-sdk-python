"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ContextKeySelectors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.context_key_selector

ContextKeySelectors: TypeAlias = list[
    "aws_sdk_cloudtrail.types.context_key_selector.ContextKeySelector"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContextKeySelectors) -> list:
    import aws_sdk_cloudtrail.types.context_key_selector

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudtrail.types.context_key_selector.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContextKeySelectors:
    import aws_sdk_cloudtrail.types.context_key_selector

    out: ContextKeySelectors = []
    for item in data:
        out.append(
            aws_sdk_cloudtrail.types.context_key_selector.deserialize_aws_json_1_1(item)
        )
    return out
