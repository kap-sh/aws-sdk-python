"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdatePackageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.commit_message
    import aws_sdk_opensearch.types.package_configuration
    import aws_sdk_opensearch.types.package_description
    import aws_sdk_opensearch.types.package_encryption_options
    import aws_sdk_opensearch.types.package_id
    import aws_sdk_opensearch.types.package_source


class UpdatePackageRequest(TypedDict):
    package_id: "aws_sdk_opensearch.types.package_id.PackageID"
    """<p>The unique identifier for the package.</p>"""
    package_source: "aws_sdk_opensearch.types.package_source.PackageSource"
    """<p>Amazon S3 bucket and key for the package.</p>"""
    package_description: NotRequired[
        "aws_sdk_opensearch.types.package_description.PackageDescription"
    ]
    """<p>A new description of the package.</p>"""
    commit_message: NotRequired["aws_sdk_opensearch.types.commit_message.CommitMessage"]
    """<p>Commit message for the updated file, which is shown as part of <code>GetPackageVersionHistoryResponse</code>.</p>"""
    package_configuration: NotRequired[
        "aws_sdk_opensearch.types.package_configuration.PackageConfiguration"
    ]
    """<p>The updated configuration details for a package.</p>"""
    package_encryption_options: NotRequired[
        "aws_sdk_opensearch.types.package_encryption_options.PackageEncryptionOptions"
    ]
    """<p>Encryption options for a package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageRequest) -> dict:
    out: dict = {}
    out["PackageID"] = value["package_id"]
    import aws_sdk_opensearch.types.package_source

    out["PackageSource"] = aws_sdk_opensearch.types.package_source.serialize_json(
        value["package_source"]
    )
    if "package_description" in value:
        out["PackageDescription"] = value["package_description"]
    if "commit_message" in value:
        out["CommitMessage"] = value["commit_message"]
    if "package_configuration" in value:
        import aws_sdk_opensearch.types.package_configuration

        out["PackageConfiguration"] = (
            aws_sdk_opensearch.types.package_configuration.serialize_json(
                value["package_configuration"]
            )
        )
    if "package_encryption_options" in value:
        import aws_sdk_opensearch.types.package_encryption_options

        out["PackageEncryptionOptions"] = (
            aws_sdk_opensearch.types.package_encryption_options.serialize_json(
                value["package_encryption_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePackageRequest:
    out: UpdatePackageRequest = {}  # type: ignore[typeddict-item]
    if "PackageID" in data:
        out["package_id"] = data["PackageID"]
    else:
        raise DeserializationError("UpdatePackageRequest.package_id required")
    if "PackageSource" in data:
        import aws_sdk_opensearch.types.package_source

        out["package_source"] = (
            aws_sdk_opensearch.types.package_source.deserialize_json(
                data["PackageSource"]
            )
        )
    else:
        raise DeserializationError("UpdatePackageRequest.package_source required")
    if "PackageDescription" in data:
        out["package_description"] = data["PackageDescription"]
    if "CommitMessage" in data:
        out["commit_message"] = data["CommitMessage"]
    if "PackageConfiguration" in data:
        import aws_sdk_opensearch.types.package_configuration

        out["package_configuration"] = (
            aws_sdk_opensearch.types.package_configuration.deserialize_json(
                data["PackageConfiguration"]
            )
        )
    if "PackageEncryptionOptions" in data:
        import aws_sdk_opensearch.types.package_encryption_options

        out["package_encryption_options"] = (
            aws_sdk_opensearch.types.package_encryption_options.deserialize_json(
                data["PackageEncryptionOptions"]
            )
        )
    return out
