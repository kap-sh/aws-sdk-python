"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListComponentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.boolean
    import capo_imagebuilder.types.filter_list
    import capo_imagebuilder.types.ownership
    import capo_imagebuilder.types.pagination_token
    import capo_imagebuilder.types.restricted_integer


class ListComponentsRequest(TypedDict, closed=True):
    owner: NotRequired["capo_imagebuilder.types.ownership.Ownership"]
    """<p>Filters results based on the type of owner for the component. By default, this request returns a list of components that your account owns. To see results for other types of owners, you can specify components that Amazon manages, third party components, or components that other accounts have shared with you.</p>"""
    filters: NotRequired["capo_imagebuilder.types.filter_list.FilterList"]
    """<p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>description</code> </p> </li> <li> <p> <code>name</code> </p> </li> <li> <p> <code>platform</code> </p> </li> <li> <p> <code>supportedOsVersion</code> </p> </li> <li> <p> <code>type</code> </p> </li> <li> <p> <code>version</code> </p> </li> </ul>"""
    by_name: "capo_imagebuilder.types.boolean.Boolean"
    """<p>Returns the list of components for the specified name.</p>"""
    max_results: NotRequired[
        "capo_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>Specify the maximum number of items to return in a request.</p>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentsRequest) -> dict:
    out: dict = {}
    if "owner" in value:
        import capo_imagebuilder.types.ownership

        out["owner"] = capo_imagebuilder.types.ownership.serialize_json(value["owner"])
    if "filters" in value:
        import capo_imagebuilder.types.filter_list

        out["filters"] = capo_imagebuilder.types.filter_list.serialize_json(
            value["filters"]
        )
    out["byName"] = value.get("by_name", False)
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComponentsRequest:
    out: ListComponentsRequest = {}  # type: ignore[typeddict-item]
    if "owner" in data:
        import capo_imagebuilder.types.ownership

        out["owner"] = capo_imagebuilder.types.ownership.deserialize_json(data["owner"])
    if "filters" in data:
        import capo_imagebuilder.types.filter_list

        out["filters"] = capo_imagebuilder.types.filter_list.deserialize_json(
            data["filters"]
        )
    if "byName" in data:
        out["by_name"] = data["byName"]
    else:
        out["by_name"] = False
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
