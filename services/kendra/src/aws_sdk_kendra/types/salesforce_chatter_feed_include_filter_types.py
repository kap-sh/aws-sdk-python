"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceChatterFeedIncludeFilterTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.salesforce_chatter_feed_include_filter_type

SalesforceChatterFeedIncludeFilterTypes: TypeAlias = list[
    "aws_sdk_kendra.types.salesforce_chatter_feed_include_filter_type.SalesforceChatterFeedIncludeFilterType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SalesforceChatterFeedIncludeFilterTypes) -> list:
    import aws_sdk_kendra.types.salesforce_chatter_feed_include_filter_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.salesforce_chatter_feed_include_filter_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SalesforceChatterFeedIncludeFilterTypes:
    import aws_sdk_kendra.types.salesforce_chatter_feed_include_filter_type

    out: SalesforceChatterFeedIncludeFilterTypes = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.salesforce_chatter_feed_include_filter_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
