"""Generated from Smithy shape ``com.amazonaws.securityhub#ListFindingAggregatorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.finding_aggregator_list
    import capo_securityhub.types.next_token


class ListFindingAggregatorsResponse(TypedDict, closed=True):
    finding_aggregators: NotRequired[
        "capo_securityhub.types.finding_aggregator_list.FindingAggregatorList"
    ]
    """<p>The list of finding aggregators. This operation currently only returns a single result.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>If there are more results, this is the token to provide in the next call to <code>ListFindingAggregators</code>.</p> <p>This operation currently only returns a single result. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFindingAggregatorsResponse) -> dict:
    out: dict = {}
    if "finding_aggregators" in value:
        import capo_securityhub.types.finding_aggregator_list

        out["FindingAggregators"] = (
            capo_securityhub.types.finding_aggregator_list.serialize_json(
                value["finding_aggregators"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFindingAggregatorsResponse:
    out: ListFindingAggregatorsResponse = {}  # type: ignore[typeddict-item]
    if "FindingAggregators" in data:
        import capo_securityhub.types.finding_aggregator_list

        out["finding_aggregators"] = (
            capo_securityhub.types.finding_aggregator_list.deserialize_json(
                data["FindingAggregators"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
