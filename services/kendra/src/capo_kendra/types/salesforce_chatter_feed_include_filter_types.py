"""Generated from Smithy shape ``com.amazonaws.kendra#SalesforceChatterFeedIncludeFilterTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.salesforce_chatter_feed_include_filter_type

SalesforceChatterFeedIncludeFilterTypes: TypeAlias = list[
    "capo_kendra.types.salesforce_chatter_feed_include_filter_type.SalesforceChatterFeedIncludeFilterType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SalesforceChatterFeedIncludeFilterTypes) -> list:
    import capo_kendra.types.salesforce_chatter_feed_include_filter_type

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.salesforce_chatter_feed_include_filter_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SalesforceChatterFeedIncludeFilterTypes:
    import capo_kendra.types.salesforce_chatter_feed_include_filter_type

    out: SalesforceChatterFeedIncludeFilterTypes = []
    for item in data:
        out.append(
            capo_kendra.types.salesforce_chatter_feed_include_filter_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
