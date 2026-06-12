"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpdatePackageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.commit_message
    import aws_sdk_elasticsearch_service.types.package_description
    import aws_sdk_elasticsearch_service.types.package_id
    import aws_sdk_elasticsearch_service.types.package_source


class UpdatePackageRequest(TypedDict):
    package_id: "aws_sdk_elasticsearch_service.types.package_id.PackageID"
    """<p>Unique identifier for the package.</p>"""
    package_source: "aws_sdk_elasticsearch_service.types.package_source.PackageSource"
    package_description: NotRequired[
        "aws_sdk_elasticsearch_service.types.package_description.PackageDescription"
    ]
    """<p>New description of the package.</p>"""
    commit_message: NotRequired[
        "aws_sdk_elasticsearch_service.types.commit_message.CommitMessage"
    ]
    """<p>An info message for the new version which will be shown as part of <code>GetPackageVersionHistoryResponse</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageRequest) -> dict:
    out: dict = {}
    out["PackageID"] = value["package_id"]
    import aws_sdk_elasticsearch_service.types.package_source

    out["PackageSource"] = (
        aws_sdk_elasticsearch_service.types.package_source.serialize_json(
            value["package_source"]
        )
    )
    if "package_description" in value:
        out["PackageDescription"] = value["package_description"]
    if "commit_message" in value:
        out["CommitMessage"] = value["commit_message"]
    return out


def deserialize_json(data: dict) -> UpdatePackageRequest:
    out: UpdatePackageRequest = {}  # type: ignore[typeddict-item]
    if "PackageID" in data:
        out["package_id"] = data["PackageID"]
    else:
        raise DeserializationError("UpdatePackageRequest.package_id required")
    if "PackageSource" in data:
        import aws_sdk_elasticsearch_service.types.package_source

        out["package_source"] = (
            aws_sdk_elasticsearch_service.types.package_source.deserialize_json(
                data["PackageSource"]
            )
        )
    else:
        raise DeserializationError("UpdatePackageRequest.package_source required")
    if "PackageDescription" in data:
        out["package_description"] = data["PackageDescription"]
    if "CommitMessage" in data:
        out["commit_message"] = data["CommitMessage"]
    return out
