"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetEventConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.aggregation_configurations
    import capo_cloudtrail.types.context_key_selectors
    import capo_cloudtrail.types.event_data_store_arn
    import capo_cloudtrail.types.max_event_size
    import capo_cloudtrail.types.string


class GetEventConfigurationResponse(TypedDict, closed=True):
    trail_arn: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the trail for which the event configuration settings are returned.</p>"""
    event_data_store_arn: NotRequired[
        "capo_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p>The Amazon Resource Name (ARN) or ID suffix of the ARN of the event data store for which the event configuration settings are returned.</p>"""
    max_event_size: NotRequired["capo_cloudtrail.types.max_event_size.MaxEventSize"]
    """<p>The maximum allowed size for events stored in the specified event data store.</p>"""
    context_key_selectors: NotRequired[
        "capo_cloudtrail.types.context_key_selectors.ContextKeySelectors"
    ]
    """<p>The list of context key selectors that are configured for the event data store.</p>"""
    aggregation_configurations: NotRequired[
        "capo_cloudtrail.types.aggregation_configurations.AggregationConfigurations"
    ]
    """<p>The list of aggregation configurations that are configured for the trail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEventConfigurationResponse) -> dict:
    out: dict = {}
    if "trail_arn" in value:
        out["TrailARN"] = value["trail_arn"]
    if "event_data_store_arn" in value:
        out["EventDataStoreArn"] = value["event_data_store_arn"]
    if "max_event_size" in value:
        import capo_cloudtrail.types.max_event_size

        out["MaxEventSize"] = (
            capo_cloudtrail.types.max_event_size.serialize_aws_json_1_1(
                value["max_event_size"]
            )
        )
    if "context_key_selectors" in value:
        import capo_cloudtrail.types.context_key_selectors

        out["ContextKeySelectors"] = (
            capo_cloudtrail.types.context_key_selectors.serialize_aws_json_1_1(
                value["context_key_selectors"]
            )
        )
    if "aggregation_configurations" in value:
        import capo_cloudtrail.types.aggregation_configurations

        out["AggregationConfigurations"] = (
            capo_cloudtrail.types.aggregation_configurations.serialize_aws_json_1_1(
                value["aggregation_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEventConfigurationResponse:
    out: GetEventConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "TrailARN" in data:
        out["trail_arn"] = data["TrailARN"]
    if "EventDataStoreArn" in data:
        out["event_data_store_arn"] = data["EventDataStoreArn"]
    if "MaxEventSize" in data:
        import capo_cloudtrail.types.max_event_size

        out["max_event_size"] = (
            capo_cloudtrail.types.max_event_size.deserialize_aws_json_1_1(
                data["MaxEventSize"]
            )
        )
    if "ContextKeySelectors" in data:
        import capo_cloudtrail.types.context_key_selectors

        out["context_key_selectors"] = (
            capo_cloudtrail.types.context_key_selectors.deserialize_aws_json_1_1(
                data["ContextKeySelectors"]
            )
        )
    if "AggregationConfigurations" in data:
        import capo_cloudtrail.types.aggregation_configurations

        out["aggregation_configurations"] = (
            capo_cloudtrail.types.aggregation_configurations.deserialize_aws_json_1_1(
                data["AggregationConfigurations"]
            )
        )
    return out
