"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ListRequesterGatewaysResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id_list


class ListRequesterGatewaysResponse(TypedDict):
    gateway_ids: NotRequired["aws_sdk_rtbfabric.types.gateway_id_list.GatewayIdList"]
    """<p>The unique identifier of the gateways.</p>"""
    next_token: NotRequired["str"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRequesterGatewaysResponse) -> dict:
    out: dict = {}
    if "gateway_ids" in value:
        import aws_sdk_rtbfabric.types.gateway_id_list

        out["gatewayIds"] = aws_sdk_rtbfabric.types.gateway_id_list.serialize_json(
            value["gateway_ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRequesterGatewaysResponse:
    out: ListRequesterGatewaysResponse = {}  # type: ignore[typeddict-item]
    if "gatewayIds" in data:
        import aws_sdk_rtbfabric.types.gateway_id_list

        out["gateway_ids"] = aws_sdk_rtbfabric.types.gateway_id_list.deserialize_json(
            data["gatewayIds"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
