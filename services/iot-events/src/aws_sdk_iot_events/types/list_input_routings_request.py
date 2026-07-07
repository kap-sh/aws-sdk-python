"""Generated from Smithy shape ``com.amazonaws.iotevents#ListInputRoutingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.input_identifier
    import aws_sdk_iot_events.types.max_results
    import aws_sdk_iot_events.types.next_token


class ListInputRoutingsRequest(TypedDict, closed=True):
    input_identifier: "aws_sdk_iot_events.types.input_identifier.InputIdentifier"
    """<p> The identifer of the routed input. </p>"""
    max_results: NotRequired["aws_sdk_iot_events.types.max_results.MaxResults"]
    """<p> The maximum number of results to be returned per request. </p>"""
    next_token: NotRequired["aws_sdk_iot_events.types.next_token.NextToken"]
    """<p> The token that you can use to return the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInputRoutingsRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_events.types.input_identifier

    out["inputIdentifier"] = aws_sdk_iot_events.types.input_identifier.serialize_json(
        value["input_identifier"]
    )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInputRoutingsRequest:
    out: ListInputRoutingsRequest = {}  # type: ignore[typeddict-item]
    if "inputIdentifier" in data:
        import aws_sdk_iot_events.types.input_identifier

        out["input_identifier"] = (
            aws_sdk_iot_events.types.input_identifier.deserialize_json(
                data["inputIdentifier"]
            )
        )
    else:
        raise DeserializationError("ListInputRoutingsRequest.input_identifier required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
