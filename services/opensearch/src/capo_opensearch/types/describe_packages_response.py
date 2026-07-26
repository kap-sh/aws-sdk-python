"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribePackagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.package_details_list
    import capo_opensearch.types.string


class DescribePackagesResponse(TypedDict, closed=True):
    package_details_list: NotRequired[
        "capo_opensearch.types.package_details_list.PackageDetailsList"
    ]
    """<p>Basic information about a package.</p>"""
    next_token: NotRequired["capo_opensearch.types.string.String"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackagesResponse) -> dict:
    out: dict = {}
    if "package_details_list" in value:
        import capo_opensearch.types.package_details_list

        out["PackageDetailsList"] = (
            capo_opensearch.types.package_details_list.serialize_json(
                value["package_details_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribePackagesResponse:
    out: DescribePackagesResponse = {}  # type: ignore[typeddict-item]
    if "PackageDetailsList" in data:
        import capo_opensearch.types.package_details_list

        out["package_details_list"] = (
            capo_opensearch.types.package_details_list.deserialize_json(
                data["PackageDetailsList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
