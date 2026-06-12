"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetEventSelectorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.advanced_event_selectors
    import aws_sdk_cloudtrail.types.event_selectors
    import aws_sdk_cloudtrail.types.string


class GetEventSelectorsResponse(TypedDict):
    trail_arn: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The specified trail ARN that has the event selectors.</p>"""
    event_selectors: NotRequired[
        "aws_sdk_cloudtrail.types.event_selectors.EventSelectors"
    ]
    """<p>The event selectors that are configured for the trail.</p>"""
    advanced_event_selectors: NotRequired[
        "aws_sdk_cloudtrail.types.advanced_event_selectors.AdvancedEventSelectors"
    ]
    """<p> The advanced event selectors that are configured for the trail. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEventSelectorsResponse) -> dict:
    out: dict = {}
    if "trail_arn" in value:
        out["TrailARN"] = value["trail_arn"]
    if "event_selectors" in value:
        import aws_sdk_cloudtrail.types.event_selectors

        out["EventSelectors"] = (
            aws_sdk_cloudtrail.types.event_selectors.serialize_aws_json_1_1(
                value["event_selectors"]
            )
        )
    if "advanced_event_selectors" in value:
        import aws_sdk_cloudtrail.types.advanced_event_selectors

        out["AdvancedEventSelectors"] = (
            aws_sdk_cloudtrail.types.advanced_event_selectors.serialize_aws_json_1_1(
                value["advanced_event_selectors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEventSelectorsResponse:
    out: GetEventSelectorsResponse = {}  # type: ignore[typeddict-item]
    if "TrailARN" in data:
        out["trail_arn"] = data["TrailARN"]
    if "EventSelectors" in data:
        import aws_sdk_cloudtrail.types.event_selectors

        out["event_selectors"] = (
            aws_sdk_cloudtrail.types.event_selectors.deserialize_aws_json_1_1(
                data["EventSelectors"]
            )
        )
    if "AdvancedEventSelectors" in data:
        import aws_sdk_cloudtrail.types.advanced_event_selectors

        out["advanced_event_selectors"] = (
            aws_sdk_cloudtrail.types.advanced_event_selectors.deserialize_aws_json_1_1(
                data["AdvancedEventSelectors"]
            )
        )
    return out
