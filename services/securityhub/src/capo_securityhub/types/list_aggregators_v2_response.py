"""Generated from Smithy shape ``com.amazonaws.securityhub#ListAggregatorsV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aggregator_v2_list
    import capo_securityhub.types.next_token


class ListAggregatorsV2Response(TypedDict, closed=True):
    aggregators_v2: NotRequired[
        "capo_securityhub.types.aggregator_v2_list.AggregatorV2List"
    ]
    """<p>An array of aggregators.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results. Otherwise, this parameter is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAggregatorsV2Response) -> dict:
    out: dict = {}
    if "aggregators_v2" in value:
        import capo_securityhub.types.aggregator_v2_list

        out["AggregatorsV2"] = capo_securityhub.types.aggregator_v2_list.serialize_json(
            value["aggregators_v2"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAggregatorsV2Response:
    out: ListAggregatorsV2Response = {}  # type: ignore[typeddict-item]
    if "AggregatorsV2" in data:
        import capo_securityhub.types.aggregator_v2_list

        out["aggregators_v2"] = (
            capo_securityhub.types.aggregator_v2_list.deserialize_json(
                data["AggregatorsV2"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
