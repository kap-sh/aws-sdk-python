"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListGatewayInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_listed_gateway_instance


class ListGatewayInstancesResponse(TypedDict, closed=True):
    instances: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_listed_gateway_instance.__listOfListedGatewayInstance"
    ]
    """<p> A list of instance summaries.</p>"""
    next_token: NotRequired["str"]
    """<p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListInstances</code> request with MaxResults set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListInstances</code> request a second time and specify the <code>NextToken</code> value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGatewayInstancesResponse) -> dict:
    out: dict = {}
    if "instances" in value:
        import aws_sdk_mediaconnect.types.__list_of_listed_gateway_instance

        out["instances"] = (
            aws_sdk_mediaconnect.types.__list_of_listed_gateway_instance.serialize_json(
                value["instances"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGatewayInstancesResponse:
    out: ListGatewayInstancesResponse = {}  # type: ignore[typeddict-item]
    if "instances" in data:
        import aws_sdk_mediaconnect.types.__list_of_listed_gateway_instance

        out["instances"] = (
            aws_sdk_mediaconnect.types.__list_of_listed_gateway_instance.deserialize_json(
                data["instances"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
