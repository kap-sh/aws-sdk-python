"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListFleetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.fleet_summaries
    import capo_iotfleetwise.types.next_token


class ListFleetsResponse(TypedDict, closed=True):
    fleet_summaries: NotRequired[
        "capo_iotfleetwise.types.fleet_summaries.fleetSummaries"
    ]
    """<p> A list of information for each fleet. </p>"""
    next_token: NotRequired["capo_iotfleetwise.types.next_token.nextToken"]
    """<p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFleetsResponse) -> dict:
    out: dict = {}
    if "fleet_summaries" in value:
        import capo_iotfleetwise.types.fleet_summaries

        out["fleetSummaries"] = (
            capo_iotfleetwise.types.fleet_summaries.serialize_aws_json_1_0(
                value["fleet_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFleetsResponse:
    out: ListFleetsResponse = {}  # type: ignore[typeddict-item]
    if "fleetSummaries" in data:
        import capo_iotfleetwise.types.fleet_summaries

        out["fleet_summaries"] = (
            capo_iotfleetwise.types.fleet_summaries.deserialize_aws_json_1_0(
                data["fleetSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
