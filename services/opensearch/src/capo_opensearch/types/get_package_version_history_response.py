"""Generated from Smithy shape ``com.amazonaws.opensearch#GetPackageVersionHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.package_id
    import capo_opensearch.types.package_version_history_list
    import capo_opensearch.types.string


class GetPackageVersionHistoryResponse(TypedDict, closed=True):
    package_id: NotRequired["capo_opensearch.types.package_id.PackageID"]
    """<p>The unique identifier of the package.</p>"""
    package_version_history_list: NotRequired[
        "capo_opensearch.types.package_version_history_list.PackageVersionHistoryList"
    ]
    """<p>A list of package versions, along with their creation time and commit message.</p>"""
    next_token: NotRequired["capo_opensearch.types.string.String"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPackageVersionHistoryResponse) -> dict:
    out: dict = {}
    if "package_id" in value:
        out["PackageID"] = value["package_id"]
    if "package_version_history_list" in value:
        import capo_opensearch.types.package_version_history_list

        out["PackageVersionHistoryList"] = (
            capo_opensearch.types.package_version_history_list.serialize_json(
                value["package_version_history_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetPackageVersionHistoryResponse:
    out: GetPackageVersionHistoryResponse = {}  # type: ignore[typeddict-item]
    if "PackageID" in data:
        out["package_id"] = data["PackageID"]
    if "PackageVersionHistoryList" in data:
        import capo_opensearch.types.package_version_history_list

        out["package_version_history_list"] = (
            capo_opensearch.types.package_version_history_list.deserialize_json(
                data["PackageVersionHistoryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
