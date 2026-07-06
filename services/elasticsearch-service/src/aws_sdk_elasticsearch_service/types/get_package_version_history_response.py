"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#GetPackageVersionHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.package_id
    import aws_sdk_elasticsearch_service.types.package_version_history_list
    import aws_sdk_elasticsearch_service.types.string


class GetPackageVersionHistoryResponse(TypedDict, closed=True):
    package_id: NotRequired["aws_sdk_elasticsearch_service.types.package_id.PackageID"]
    package_version_history_list: NotRequired[
        "aws_sdk_elasticsearch_service.types.package_version_history_list.PackageVersionHistoryList"
    ]
    """<p>List of <code>PackageVersionHistory</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: GetPackageVersionHistoryResponse) -> dict:
    out: dict = {}
    if "package_id" in value:
        out["PackageID"] = value["package_id"]
    if "package_version_history_list" in value:
        import aws_sdk_elasticsearch_service.types.package_version_history_list

        out["PackageVersionHistoryList"] = (
            aws_sdk_elasticsearch_service.types.package_version_history_list.serialize_json(
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
        import aws_sdk_elasticsearch_service.types.package_version_history_list

        out["package_version_history_list"] = (
            aws_sdk_elasticsearch_service.types.package_version_history_list.deserialize_json(
                data["PackageVersionHistoryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
