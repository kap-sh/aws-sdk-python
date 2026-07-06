"""Generated from Smithy shape ``com.amazonaws.cloudtrail#PutEventSelectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.advanced_event_selectors
    import aws_sdk_cloudtrail.types.event_selectors
    import aws_sdk_cloudtrail.types.string


class PutEventSelectorsResponse(TypedDict, closed=True):
    trail_arn: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>Specifies the ARN of the trail that was updated with event selectors. The following is the format of a trail ARN.</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p>"""
    event_selectors: NotRequired[
        "aws_sdk_cloudtrail.types.event_selectors.EventSelectors"
    ]
    """<p>Specifies the event selectors configured for your trail.</p>"""
    advanced_event_selectors: NotRequired[
        "aws_sdk_cloudtrail.types.advanced_event_selectors.AdvancedEventSelectors"
    ]
    """<p>Specifies the advanced event selectors configured for your trail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEventSelectorsResponse) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> PutEventSelectorsResponse:
    out: PutEventSelectorsResponse = {}  # type: ignore[typeddict-item]
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
