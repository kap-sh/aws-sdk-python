"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListInfrastructureConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.filter_list
    import capo_imagebuilder.types.pagination_token
    import capo_imagebuilder.types.restricted_integer


class ListInfrastructureConfigurationsRequest(TypedDict, closed=True):
    filters: NotRequired["capo_imagebuilder.types.filter_list.FilterList"]
    """<p>You can filter on <code>name</code> to streamline results.</p>"""
    max_results: NotRequired[
        "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>Specify the maximum number of items to return in a request.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInfrastructureConfigurationsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_imagebuilder.types.filter_list

        out["filters"] = capo_imagebuilder.types.filter_list.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInfrastructureConfigurationsRequest:
    out: ListInfrastructureConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import capo_imagebuilder.types.filter_list

        out["filters"] = capo_imagebuilder.types.filter_list.deserialize_json(
            data["filters"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
