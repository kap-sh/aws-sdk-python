"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PackageVersionHistory``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.commit_message
    import aws_sdk_elasticsearch_service.types.created_at
    import aws_sdk_elasticsearch_service.types.package_version


class PackageVersionHistory(TypedDict):
    package_version: NotRequired[
        "aws_sdk_elasticsearch_service.types.package_version.PackageVersion"
    ]
    """<p>Version of the package.</p>"""
    commit_message: NotRequired[
        "aws_sdk_elasticsearch_service.types.commit_message.CommitMessage"
    ]
    """<p>A message associated with the version.</p>"""
    created_at: NotRequired["aws_sdk_elasticsearch_service.types.created_at.CreatedAt"]
    """<p>Timestamp which tells creation time of the package version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionHistory) -> dict:
    out: dict = {}
    if "package_version" in value:
        out["PackageVersion"] = value["package_version"]
    if "commit_message" in value:
        out["CommitMessage"] = value["commit_message"]
    if "created_at" in value:
        import aws_sdk_elasticsearch_service.types.created_at

        out["CreatedAt"] = (
            aws_sdk_elasticsearch_service.types.created_at.serialize_json(
                value["created_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> PackageVersionHistory:
    out: PackageVersionHistory = {}  # type: ignore[typeddict-item]
    if "PackageVersion" in data:
        out["package_version"] = data["PackageVersion"]
    if "CommitMessage" in data:
        out["commit_message"] = data["CommitMessage"]
    if "CreatedAt" in data:
        import aws_sdk_elasticsearch_service.types.created_at

        out["created_at"] = (
            aws_sdk_elasticsearch_service.types.created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    return out
