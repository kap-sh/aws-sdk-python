"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListGatewaysResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.gateway_summaries
    import aws_sdk_iotsitewise.types.next_token


class ListGatewaysResponse(TypedDict):
    gateway_summaries: "aws_sdk_iotsitewise.types.gateway_summaries.GatewaySummaries"
    """<p>A list that summarizes each gateway.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGatewaysResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.gateway_summaries

    out["gatewaySummaries"] = (
        aws_sdk_iotsitewise.types.gateway_summaries.serialize_json(
            value["gateway_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGatewaysResponse:
    out: ListGatewaysResponse = {}  # type: ignore[typeddict-item]
    if "gatewaySummaries" in data:
        import aws_sdk_iotsitewise.types.gateway_summaries

        out["gateway_summaries"] = (
            aws_sdk_iotsitewise.types.gateway_summaries.deserialize_json(
                data["gatewaySummaries"]
            )
        )
    else:
        raise DeserializationError("ListGatewaysResponse.gateway_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
