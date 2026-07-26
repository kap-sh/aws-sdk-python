"""Generated from Smithy shape ``com.amazonaws.sustainability#GetEstimatedCarbonEmissionsDimensionValuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sustainability.types.dimension_entry_list
    import capo_sustainability.types.next_token


class GetEstimatedCarbonEmissionsDimensionValuesResponse(TypedDict, closed=True):
    results: NotRequired[
        "capo_sustainability.types.dimension_entry_list.DimensionEntryList"
    ]
    """<p>The list of possible dimensions over which the emissions data is aggregated.</p>"""
    next_token: NotRequired["capo_sustainability.types.next_token.NextToken"]
    """<p>The pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEstimatedCarbonEmissionsDimensionValuesResponse) -> dict:
    out: dict = {}
    if "results" in value:
        import capo_sustainability.types.dimension_entry_list

        out["Results"] = capo_sustainability.types.dimension_entry_list.serialize_json(
            value["results"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetEstimatedCarbonEmissionsDimensionValuesResponse:
    out: GetEstimatedCarbonEmissionsDimensionValuesResponse = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import capo_sustainability.types.dimension_entry_list

        out["results"] = (
            capo_sustainability.types.dimension_entry_list.deserialize_json(
                data["Results"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
