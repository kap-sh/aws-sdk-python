"""Generated from Smithy shape ``com.amazonaws.personalize#ListFiltersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.filters
    import capo_personalize.types.next_token


class ListFiltersResponse(TypedDict, closed=True):
    filters: NotRequired["capo_personalize.types.filters.Filters"]
    """<p>A list of returned filters.</p>"""
    next_token: NotRequired["capo_personalize.types.next_token.NextToken"]
    """<p>A token for getting the next set of filters (if they exist).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFiltersResponse) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_personalize.types.filters

        out["Filters"] = capo_personalize.types.filters.serialize_aws_json_1_1(
            value["filters"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFiltersResponse:
    out: ListFiltersResponse = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import capo_personalize.types.filters

        out["filters"] = capo_personalize.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
