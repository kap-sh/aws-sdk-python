"""Generated from Smithy shape ``com.amazonaws.cloudtrail#PutEventConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.aggregation_configurations
    import aws_sdk_cloudtrail.types.context_key_selectors
    import aws_sdk_cloudtrail.types.event_data_store_arn
    import aws_sdk_cloudtrail.types.max_event_size
    import aws_sdk_cloudtrail.types.string


class PutEventConfigurationResponse(TypedDict):
    trail_arn: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the trail that has aggregation enabled.</p>"""
    event_data_store_arn: NotRequired[
        "aws_sdk_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p>The Amazon Resource Name (ARN) or ID suffix of the ARN of the event data store for which the event configuration settings were updated.</p>"""
    max_event_size: NotRequired["aws_sdk_cloudtrail.types.max_event_size.MaxEventSize"]
    """<p>The maximum allowed size for events stored in the specified event data store.</p>"""
    context_key_selectors: NotRequired[
        "aws_sdk_cloudtrail.types.context_key_selectors.ContextKeySelectors"
    ]
    """<p>The list of context key selectors that are configured for the event data store.</p>"""
    aggregation_configurations: NotRequired[
        "aws_sdk_cloudtrail.types.aggregation_configurations.AggregationConfigurations"
    ]
    """<p>A list of aggregation configurations that are configured for the trail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEventConfigurationResponse) -> dict:
    out: dict = {}
    if "trail_arn" in value:
        out["TrailARN"] = value["trail_arn"]
    if "event_data_store_arn" in value:
        out["EventDataStoreArn"] = value["event_data_store_arn"]
    if "max_event_size" in value:
        import aws_sdk_cloudtrail.types.max_event_size

        out["MaxEventSize"] = (
            aws_sdk_cloudtrail.types.max_event_size.serialize_aws_json_1_1(
                value["max_event_size"]
            )
        )
    if "context_key_selectors" in value:
        import aws_sdk_cloudtrail.types.context_key_selectors

        out["ContextKeySelectors"] = (
            aws_sdk_cloudtrail.types.context_key_selectors.serialize_aws_json_1_1(
                value["context_key_selectors"]
            )
        )
    if "aggregation_configurations" in value:
        import aws_sdk_cloudtrail.types.aggregation_configurations

        out["AggregationConfigurations"] = (
            aws_sdk_cloudtrail.types.aggregation_configurations.serialize_aws_json_1_1(
                value["aggregation_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutEventConfigurationResponse:
    out: PutEventConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "TrailARN" in data:
        out["trail_arn"] = data["TrailARN"]
    if "EventDataStoreArn" in data:
        out["event_data_store_arn"] = data["EventDataStoreArn"]
    if "MaxEventSize" in data:
        import aws_sdk_cloudtrail.types.max_event_size

        out["max_event_size"] = (
            aws_sdk_cloudtrail.types.max_event_size.deserialize_aws_json_1_1(
                data["MaxEventSize"]
            )
        )
    if "ContextKeySelectors" in data:
        import aws_sdk_cloudtrail.types.context_key_selectors

        out["context_key_selectors"] = (
            aws_sdk_cloudtrail.types.context_key_selectors.deserialize_aws_json_1_1(
                data["ContextKeySelectors"]
            )
        )
    if "AggregationConfigurations" in data:
        import aws_sdk_cloudtrail.types.aggregation_configurations

        out["aggregation_configurations"] = (
            aws_sdk_cloudtrail.types.aggregation_configurations.deserialize_aws_json_1_1(
                data["AggregationConfigurations"]
            )
        )
    return out
