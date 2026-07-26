"""Generated from Smithy shape ``com.amazonaws.panorama#ListNodesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.max_size25
    import capo_panorama.types.node_category
    import capo_panorama.types.node_package_name
    import capo_panorama.types.node_package_patch_version
    import capo_panorama.types.node_package_version
    import capo_panorama.types.package_owner_account
    import capo_panorama.types.token


class ListNodesRequest(TypedDict, closed=True):
    category: NotRequired["capo_panorama.types.node_category.NodeCategory"]
    """<p>Search for nodes by category.</p>"""
    owner_account: NotRequired[
        "capo_panorama.types.package_owner_account.PackageOwnerAccount"
    ]
    """<p>Search for nodes by the account ID of the nodes' owner.</p>"""
    package_name: NotRequired["capo_panorama.types.node_package_name.NodePackageName"]
    """<p>Search for nodes by name.</p>"""
    package_version: NotRequired[
        "capo_panorama.types.node_package_version.NodePackageVersion"
    ]
    """<p>Search for nodes by version.</p>"""
    patch_version: NotRequired[
        "capo_panorama.types.node_package_patch_version.NodePackagePatchVersion"
    ]
    """<p>Search for nodes by patch version.</p>"""
    next_token: NotRequired["capo_panorama.types.token.Token"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: "capo_panorama.types.max_size25.MaxSize25"
    """<p>The maximum number of nodes to return in one page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNodesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNodesRequest:
    out: ListNodesRequest = {}  # type: ignore[typeddict-item]
    return out
