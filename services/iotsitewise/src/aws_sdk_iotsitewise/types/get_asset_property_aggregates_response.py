"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetAssetPropertyAggregatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.aggregated_values
    import aws_sdk_iotsitewise.types.next_token


class GetAssetPropertyAggregatesResponse(TypedDict, closed=True):
    aggregated_values: "aws_sdk_iotsitewise.types.aggregated_values.AggregatedValues"
    """<p>The requested aggregated values.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssetPropertyAggregatesResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.aggregated_values

    out["aggregatedValues"] = (
        aws_sdk_iotsitewise.types.aggregated_values.serialize_json(
            value["aggregated_values"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetAssetPropertyAggregatesResponse:
    out: GetAssetPropertyAggregatesResponse = {}  # type: ignore[typeddict-item]
    if "aggregatedValues" in data:
        import aws_sdk_iotsitewise.types.aggregated_values

        out["aggregated_values"] = (
            aws_sdk_iotsitewise.types.aggregated_values.deserialize_json(
                data["aggregatedValues"]
            )
        )
    else:
        raise DeserializationError(
            "GetAssetPropertyAggregatesResponse.aggregated_values required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
