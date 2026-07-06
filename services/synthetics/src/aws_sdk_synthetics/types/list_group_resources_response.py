"""Generated from Smithy shape ``com.amazonaws.synthetics#ListGroupResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.pagination_token
    import aws_sdk_synthetics.types.string_list


class ListGroupResourcesResponse(TypedDict, closed=True):
    resources: NotRequired["aws_sdk_synthetics.types.string_list.StringList"]
    """<p>An array of ARNs. These ARNs are for the canaries that are associated with the group.</p>"""
    next_token: NotRequired["aws_sdk_synthetics.types.pagination_token.PaginationToken"]
    """<p>A token that indicates that there is more data available. You can use this token in a subsequent <code>ListGroupResources</code> operation to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupResourcesResponse) -> dict:
    out: dict = {}
    if "resources" in value:
        import aws_sdk_synthetics.types.string_list

        out["Resources"] = aws_sdk_synthetics.types.string_list.serialize_json(
            value["resources"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGroupResourcesResponse:
    out: ListGroupResourcesResponse = {}  # type: ignore[typeddict-item]
    if "Resources" in data:
        import aws_sdk_synthetics.types.string_list

        out["resources"] = aws_sdk_synthetics.types.string_list.deserialize_json(
            data["Resources"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
