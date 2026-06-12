"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageVersionHistory``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.commit_message
    import aws_sdk_opensearch.types.created_at
    import aws_sdk_opensearch.types.package_configuration
    import aws_sdk_opensearch.types.package_version
    import aws_sdk_opensearch.types.plugin_properties


class PackageVersionHistory(TypedDict):
    package_version: NotRequired[
        "aws_sdk_opensearch.types.package_version.PackageVersion"
    ]
    """<p>The package version.</p>"""
    commit_message: NotRequired["aws_sdk_opensearch.types.commit_message.CommitMessage"]
    """<p>A message associated with the package version when it was uploaded.</p>"""
    created_at: NotRequired["aws_sdk_opensearch.types.created_at.CreatedAt"]
    """<p>The date and time when the package was created.</p>"""
    plugin_properties: NotRequired[
        "aws_sdk_opensearch.types.plugin_properties.PluginProperties"
    ]
    """<p>Additional information about plugin properties if the package is a <code>ZIP-PLUGIN</code> package.</p>"""
    package_configuration: NotRequired[
        "aws_sdk_opensearch.types.package_configuration.PackageConfiguration"
    ]
    """<p>The configuration details for a specific version of a package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionHistory) -> dict:
    out: dict = {}
    if "package_version" in value:
        out["PackageVersion"] = value["package_version"]
    if "commit_message" in value:
        out["CommitMessage"] = value["commit_message"]
    if "created_at" in value:
        import aws_sdk_opensearch.types.created_at

        out["CreatedAt"] = aws_sdk_opensearch.types.created_at.serialize_json(
            value["created_at"]
        )
    if "plugin_properties" in value:
        import aws_sdk_opensearch.types.plugin_properties

        out["PluginProperties"] = (
            aws_sdk_opensearch.types.plugin_properties.serialize_json(
                value["plugin_properties"]
            )
        )
    if "package_configuration" in value:
        import aws_sdk_opensearch.types.package_configuration

        out["PackageConfiguration"] = (
            aws_sdk_opensearch.types.package_configuration.serialize_json(
                value["package_configuration"]
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
        import aws_sdk_opensearch.types.created_at

        out["created_at"] = aws_sdk_opensearch.types.created_at.deserialize_json(
            data["CreatedAt"]
        )
    if "PluginProperties" in data:
        import aws_sdk_opensearch.types.plugin_properties

        out["plugin_properties"] = (
            aws_sdk_opensearch.types.plugin_properties.deserialize_json(
                data["PluginProperties"]
            )
        )
    if "PackageConfiguration" in data:
        import aws_sdk_opensearch.types.package_configuration

        out["package_configuration"] = (
            aws_sdk_opensearch.types.package_configuration.deserialize_json(
                data["PackageConfiguration"]
            )
        )
    return out
