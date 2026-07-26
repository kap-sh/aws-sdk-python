"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListComponentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.component_version_list
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.pagination_token


class ListComponentsResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    component_version_list: NotRequired[
        "capo_imagebuilder.types.component_version_list.ComponentVersionList"
    ]
    """<p>The list of component semantic versions.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> </note>"""
    next_token: NotRequired["capo_imagebuilder.types.pagination_token.PaginationToken"]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentsResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "component_version_list" in value:
        import capo_imagebuilder.types.component_version_list

        out["componentVersionList"] = (
            capo_imagebuilder.types.component_version_list.serialize_json(
                value["component_version_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComponentsResponse:
    out: ListComponentsResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "componentVersionList" in data:
        import capo_imagebuilder.types.component_version_list

        out["component_version_list"] = (
            capo_imagebuilder.types.component_version_list.deserialize_json(
                data["componentVersionList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
