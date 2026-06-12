"""Generated from Smithy shape ``com.amazonaws.cloudtrail#PutEventConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.aggregation_configurations
    import aws_sdk_cloudtrail.types.context_key_selectors
    import aws_sdk_cloudtrail.types.max_event_size
    import aws_sdk_cloudtrail.types.string


class PutEventConfigurationRequest(TypedDict):
    trail_name: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The name of the trail for which you want to update event configuration settings.</p>"""
    event_data_store: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The Amazon Resource Name (ARN) or ID suffix of the ARN of the event data store for which event configuration settings are updated.</p>"""
    max_event_size: NotRequired["aws_sdk_cloudtrail.types.max_event_size.MaxEventSize"]
    """<p>The maximum allowed size for events to be stored in the specified event data store. If you are using context key selectors, MaxEventSize must be set to Large.</p>"""
    context_key_selectors: NotRequired[
        "aws_sdk_cloudtrail.types.context_key_selectors.ContextKeySelectors"
    ]
    """<p>A list of context key selectors that will be included to provide enriched event data.</p>"""
    aggregation_configurations: NotRequired[
        "aws_sdk_cloudtrail.types.aggregation_configurations.AggregationConfigurations"
    ]
    """<p>The list of aggregation configurations that you want to configure for the trail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEventConfigurationRequest) -> dict:
    out: dict = {}
    if "trail_name" in value:
        out["TrailName"] = value["trail_name"]
    if "event_data_store" in value:
        out["EventDataStore"] = value["event_data_store"]
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


def deserialize_aws_json_1_1(data: dict) -> PutEventConfigurationRequest:
    out: PutEventConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "TrailName" in data:
        out["trail_name"] = data["TrailName"]
    if "EventDataStore" in data:
        out["event_data_store"] = data["EventDataStore"]
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
