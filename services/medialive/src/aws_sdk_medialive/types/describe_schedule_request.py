"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.max_results


class DescribeScheduleRequest(TypedDict, closed=True):
    channel_id: "aws_sdk_medialive.types.__string.__string"
    """Id of the channel whose schedule is being updated."""
    max_results: NotRequired["aws_sdk_medialive.types.max_results.MaxResults"]
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeScheduleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeScheduleRequest:
    out: DescribeScheduleRequest = {}  # type: ignore[typeddict-item]
    return out
