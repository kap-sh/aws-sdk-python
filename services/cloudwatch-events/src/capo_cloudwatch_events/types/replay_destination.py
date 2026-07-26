"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ReplayDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.arn
    import capo_cloudwatch_events.types.replay_destination_filters


class ReplayDestination(TypedDict, closed=True):
    arn: "capo_cloudwatch_events.types.arn.Arn"
    """<p>The ARN of the event bus to replay event to. You can replay events only to the event bus specified to create the archive.</p>"""
    filter_arns: NotRequired[
        "capo_cloudwatch_events.types.replay_destination_filters.ReplayDestinationFilters"
    ]
    """<p>A list of ARNs for rules to replay events to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplayDestination) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "filter_arns" in value:
        import capo_cloudwatch_events.types.replay_destination_filters

        out["FilterArns"] = (
            capo_cloudwatch_events.types.replay_destination_filters.serialize_aws_json_1_1(
                value["filter_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplayDestination:
    out: ReplayDestination = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ReplayDestination.arn required")
    if "FilterArns" in data:
        import capo_cloudwatch_events.types.replay_destination_filters

        out["filter_arns"] = (
            capo_cloudwatch_events.types.replay_destination_filters.deserialize_aws_json_1_1(
                data["FilterArns"]
            )
        )
    return out
