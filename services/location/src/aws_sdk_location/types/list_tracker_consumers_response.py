"""Generated from Smithy shape ``com.amazonaws.location#ListTrackerConsumersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.arn_list
    import aws_sdk_location.types.token


class ListTrackerConsumersResponse(TypedDict):
    consumer_arns: "aws_sdk_location.types.arn_list.ArnList"
    """<p>Contains the list of geofence collection ARNs associated to the tracker resource.</p>"""
    next_token: NotRequired["aws_sdk_location.types.token.Token"]
    """<p>A pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrackerConsumersResponse) -> dict:
    out: dict = {}
    import aws_sdk_location.types.arn_list

    out["ConsumerArns"] = aws_sdk_location.types.arn_list.serialize_json(
        value["consumer_arns"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTrackerConsumersResponse:
    out: ListTrackerConsumersResponse = {}  # type: ignore[typeddict-item]
    if "ConsumerArns" in data:
        import aws_sdk_location.types.arn_list

        out["consumer_arns"] = aws_sdk_location.types.arn_list.deserialize_json(
            data["ConsumerArns"]
        )
    else:
        raise DeserializationError(
            "ListTrackerConsumersResponse.consumer_arns required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
