"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListContainerRecipesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.filter_list
    import aws_sdk_imagebuilder.types.ownership
    import aws_sdk_imagebuilder.types.pagination_token
    import aws_sdk_imagebuilder.types.restricted_integer


class ListContainerRecipesRequest(TypedDict):
    owner: NotRequired["aws_sdk_imagebuilder.types.ownership.Ownership"]
    """<p>Returns container recipes belonging to the specified owner, that have been shared with you. You can omit this field to return container recipes belonging to your account.</p>"""
    filters: NotRequired["aws_sdk_imagebuilder.types.filter_list.FilterList"]
    """<p>Use the following filters to streamline results:</p> <ul> <li> <p> <code>containerType</code> </p> </li> <li> <p> <code>name</code> </p> </li> <li> <p> <code>parentImage</code> </p> </li> <li> <p> <code>platform</code> </p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_imagebuilder.types.restricted_integer.RestrictedInteger"
    ]
    """<p>Specify the maximum number of items to return in a request.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContainerRecipesRequest) -> dict:
    out: dict = {}
    if "owner" in value:
        import aws_sdk_imagebuilder.types.ownership

        out["owner"] = aws_sdk_imagebuilder.types.ownership.serialize_json(
            value["owner"]
        )
    if "filters" in value:
        import aws_sdk_imagebuilder.types.filter_list

        out["filters"] = aws_sdk_imagebuilder.types.filter_list.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContainerRecipesRequest:
    out: ListContainerRecipesRequest = {}  # type: ignore[typeddict-item]
    if "owner" in data:
        import aws_sdk_imagebuilder.types.ownership

        out["owner"] = aws_sdk_imagebuilder.types.ownership.deserialize_json(
            data["owner"]
        )
    if "filters" in data:
        import aws_sdk_imagebuilder.types.filter_list

        out["filters"] = aws_sdk_imagebuilder.types.filter_list.deserialize_json(
            data["filters"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
