"""Generated from Smithy shape ``com.amazonaws.eventbridge#ReplayDestinationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.arn

ReplayDestinationFilters: TypeAlias = list["capo_eventbridge.types.arn.Arn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplayDestinationFilters) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ReplayDestinationFilters:
    return [item for item in data if item is not None]
