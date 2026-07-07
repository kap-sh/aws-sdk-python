"""Generated from Smithy shape ``com.amazonaws.ses#DescribeConfigurationSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.configuration_set
    import aws_sdk_ses.types.delivery_options
    import aws_sdk_ses.types.event_destinations
    import aws_sdk_ses.types.reputation_options
    import aws_sdk_ses.types.tracking_options


class DescribeConfigurationSetResponse(TypedDict, closed=True):
    configuration_set: NotRequired[
        "aws_sdk_ses.types.configuration_set.ConfigurationSet"
    ]
    """<p>The configuration set object associated with the specified configuration set.</p>"""
    event_destinations: NotRequired[
        "aws_sdk_ses.types.event_destinations.EventDestinations"
    ]
    """<p>A list of event destinations associated with the configuration set. </p>"""
    tracking_options: NotRequired["aws_sdk_ses.types.tracking_options.TrackingOptions"]
    """<p>The name of the custom open and click tracking domain associated with the configuration set.</p>"""
    delivery_options: NotRequired["aws_sdk_ses.types.delivery_options.DeliveryOptions"]
    reputation_options: NotRequired[
        "aws_sdk_ses.types.reputation_options.ReputationOptions"
    ]
    """<p>An object that represents the reputation settings for the configuration set. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeConfigurationSetResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "configuration_set" in value:
        import aws_sdk_ses.types.configuration_set

        aws_sdk_ses.types.configuration_set.serialize_query(
            value["configuration_set"], pairs, f"{prefix}.ConfigurationSet"
        )
    if "event_destinations" in value:
        import aws_sdk_ses.types.event_destinations

        aws_sdk_ses.types.event_destinations.serialize_query(
            value["event_destinations"], pairs, f"{prefix}.EventDestinations"
        )
    if "tracking_options" in value:
        import aws_sdk_ses.types.tracking_options

        aws_sdk_ses.types.tracking_options.serialize_query(
            value["tracking_options"], pairs, f"{prefix}.TrackingOptions"
        )
    if "delivery_options" in value:
        import aws_sdk_ses.types.delivery_options

        aws_sdk_ses.types.delivery_options.serialize_query(
            value["delivery_options"], pairs, f"{prefix}.DeliveryOptions"
        )
    if "reputation_options" in value:
        import aws_sdk_ses.types.reputation_options

        aws_sdk_ses.types.reputation_options.serialize_query(
            value["reputation_options"], pairs, f"{prefix}.ReputationOptions"
        )


def deserialize_query(el: Element) -> DescribeConfigurationSetResponse:
    out: DescribeConfigurationSetResponse = {}  # type: ignore[typeddict-item]
    child_configuration_set = el.find("ConfigurationSet")
    if child_configuration_set is not None:
        import aws_sdk_ses.types.configuration_set

        out["configuration_set"] = (
            aws_sdk_ses.types.configuration_set.deserialize_query(
                child_configuration_set
            )
        )
    child_event_destinations = el.find("EventDestinations")
    if child_event_destinations is not None:
        import aws_sdk_ses.types.event_destinations

        out["event_destinations"] = (
            aws_sdk_ses.types.event_destinations.deserialize_query(
                child_event_destinations
            )
        )
    child_tracking_options = el.find("TrackingOptions")
    if child_tracking_options is not None:
        import aws_sdk_ses.types.tracking_options

        out["tracking_options"] = aws_sdk_ses.types.tracking_options.deserialize_query(
            child_tracking_options
        )
    child_delivery_options = el.find("DeliveryOptions")
    if child_delivery_options is not None:
        import aws_sdk_ses.types.delivery_options

        out["delivery_options"] = aws_sdk_ses.types.delivery_options.deserialize_query(
            child_delivery_options
        )
    child_reputation_options = el.find("ReputationOptions")
    if child_reputation_options is not None:
        import aws_sdk_ses.types.reputation_options

        out["reputation_options"] = (
            aws_sdk_ses.types.reputation_options.deserialize_query(
                child_reputation_options
            )
        )
    return out
