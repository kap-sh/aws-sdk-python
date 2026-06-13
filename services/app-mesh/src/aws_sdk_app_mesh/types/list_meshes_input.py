"""Generated from Smithy shape ``com.amazonaws.appmesh#ListMeshesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.list_meshes_limit


class ListMeshesInput(TypedDict):
    next_token: NotRequired["str"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListMeshes</code> request where <code>limit</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    limit: NotRequired["aws_sdk_app_mesh.types.list_meshes_limit.ListMeshesLimit"]
    """<p>The maximum number of results returned by <code>ListMeshes</code> in paginated output. When you use this parameter, <code>ListMeshes</code> returns only <code>limit</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListMeshes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListMeshes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMeshesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMeshesInput:
    out: ListMeshesInput = {}  # type: ignore[typeddict-item]
    return out
