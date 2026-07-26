"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribePackagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.package_details_list
    import capo_elasticsearch_service.types.string


class DescribePackagesResponse(TypedDict, closed=True):
    package_details_list: NotRequired[
        "capo_elasticsearch_service.types.package_details_list.PackageDetailsList"
    ]
    """<p>List of <code>PackageDetails</code> objects.</p>"""
    next_token: NotRequired["capo_elasticsearch_service.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackagesResponse) -> dict:
    out: dict = {}
    if "package_details_list" in value:
        import capo_elasticsearch_service.types.package_details_list

        out["PackageDetailsList"] = (
            capo_elasticsearch_service.types.package_details_list.serialize_json(
                value["package_details_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribePackagesResponse:
    out: DescribePackagesResponse = {}  # type: ignore[typeddict-item]
    if "PackageDetailsList" in data:
        import capo_elasticsearch_service.types.package_details_list

        out["package_details_list"] = (
            capo_elasticsearch_service.types.package_details_list.deserialize_json(
                data["PackageDetailsList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
