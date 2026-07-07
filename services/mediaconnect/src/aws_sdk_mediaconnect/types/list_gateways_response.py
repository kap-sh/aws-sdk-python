"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListGatewaysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_listed_gateway


class ListGatewaysResponse(TypedDict, closed=True):
    gateways: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_listed_gateway.__listOfListedGateway"
    ]
    """<p> A list of gateway summaries.</p>"""
    next_token: NotRequired["str"]
    """<p> The token that identifies the batch of results that you want to see. </p> <p>For example, you submit a <code>ListGateways</code> request with <code>MaxResults</code> set at 5. The service returns the first batch of results (up to 5) and a <code>NextToken</code> value. To see the next batch of results, you can submit the <code>ListGateways</code> request a second time and specify the <code>NextToken</code> value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGatewaysResponse) -> dict:
    out: dict = {}
    if "gateways" in value:
        import aws_sdk_mediaconnect.types.__list_of_listed_gateway

        out["gateways"] = (
            aws_sdk_mediaconnect.types.__list_of_listed_gateway.serialize_json(
                value["gateways"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGatewaysResponse:
    out: ListGatewaysResponse = {}  # type: ignore[typeddict-item]
    if "gateways" in data:
        import aws_sdk_mediaconnect.types.__list_of_listed_gateway

        out["gateways"] = (
            aws_sdk_mediaconnect.types.__list_of_listed_gateway.deserialize_json(
                data["gateways"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
