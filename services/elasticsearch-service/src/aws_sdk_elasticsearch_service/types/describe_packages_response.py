"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribePackagesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.package_details_list
    import aws_sdk_elasticsearch_service.types.string


class DescribePackagesResponse(TypedDict):
    package_details_list: NotRequired[
        "aws_sdk_elasticsearch_service.types.package_details_list.PackageDetailsList"
    ]
    """<p>List of <code>PackageDetails</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackagesResponse) -> dict:
    out: dict = {}
    if "package_details_list" in value:
        import aws_sdk_elasticsearch_service.types.package_details_list

        out["PackageDetailsList"] = (
            aws_sdk_elasticsearch_service.types.package_details_list.serialize_json(
                value["package_details_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribePackagesResponse:
    out: DescribePackagesResponse = {}  # type: ignore[typeddict-item]
    if "PackageDetailsList" in data:
        import aws_sdk_elasticsearch_service.types.package_details_list

        out["package_details_list"] = (
            aws_sdk_elasticsearch_service.types.package_details_list.deserialize_json(
                data["PackageDetailsList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
