"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.created_at
    import aws_sdk_opensearch.types.engine_version
    import aws_sdk_opensearch.types.error_details
    import aws_sdk_opensearch.types.last_updated
    import aws_sdk_opensearch.types.package_configuration
    import aws_sdk_opensearch.types.package_description
    import aws_sdk_opensearch.types.package_encryption_options
    import aws_sdk_opensearch.types.package_id
    import aws_sdk_opensearch.types.package_name
    import aws_sdk_opensearch.types.package_owner
    import aws_sdk_opensearch.types.package_status
    import aws_sdk_opensearch.types.package_type
    import aws_sdk_opensearch.types.package_user_list
    import aws_sdk_opensearch.types.package_vending_options
    import aws_sdk_opensearch.types.package_version
    import aws_sdk_opensearch.types.plugin_properties


class PackageDetails(TypedDict):
    package_id: NotRequired["aws_sdk_opensearch.types.package_id.PackageID"]
    """<p>The unique identifier of the package.</p>"""
    package_name: NotRequired["aws_sdk_opensearch.types.package_name.PackageName"]
    """<p>The user-specified name of the package.</p>"""
    package_type: NotRequired["aws_sdk_opensearch.types.package_type.PackageType"]
    """<p>The type of package.</p>"""
    package_description: NotRequired[
        "aws_sdk_opensearch.types.package_description.PackageDescription"
    ]
    """<p>User-specified description of the package.</p>"""
    package_status: NotRequired["aws_sdk_opensearch.types.package_status.PackageStatus"]
    """<p>The current status of the package. The available options are <code>AVAILABLE</code>, <code>COPYING</code>, <code>COPY_FAILED</code>, <code>VALIDATNG</code>, <code>VALIDATION_FAILED</code>, <code>DELETING</code>, and <code>DELETE_FAILED</code>.</p>"""
    created_at: NotRequired["aws_sdk_opensearch.types.created_at.CreatedAt"]
    """<p>The timestamp when the package was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_opensearch.types.last_updated.LastUpdated"]
    """<p>Date and time when the package was last updated.</p>"""
    available_package_version: NotRequired[
        "aws_sdk_opensearch.types.package_version.PackageVersion"
    ]
    """<p>The package version.</p>"""
    error_details: NotRequired["aws_sdk_opensearch.types.error_details.ErrorDetails"]
    """<p>Additional information if the package is in an error state. Null otherwise.</p>"""
    engine_version: NotRequired["aws_sdk_opensearch.types.engine_version.EngineVersion"]
    """<p>Version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch.</p>"""
    available_plugin_properties: NotRequired[
        "aws_sdk_opensearch.types.plugin_properties.PluginProperties"
    ]
    """<p>If the package is a <code>ZIP-PLUGIN</code> package, additional information about plugin properties.</p>"""
    available_package_configuration: NotRequired[
        "aws_sdk_opensearch.types.package_configuration.PackageConfiguration"
    ]
    """<p>This represents the available configuration parameters for the package.</p>"""
    allow_listed_user_list: NotRequired[
        "aws_sdk_opensearch.types.package_user_list.PackageUserList"
    ]
    """<p> A list of users who are allowed to view and associate the package. This field is only visible to the owner of a package.</p>"""
    package_owner: NotRequired["aws_sdk_opensearch.types.package_owner.PackageOwner"]
    """<p>The owner of the package who is allowed to create and update a package and add users to the package scope.</p>"""
    package_vending_options: NotRequired[
        "aws_sdk_opensearch.types.package_vending_options.PackageVendingOptions"
    ]
    """<p>Package Vending Options for a package.</p>"""
    package_encryption_options: NotRequired[
        "aws_sdk_opensearch.types.package_encryption_options.PackageEncryptionOptions"
    ]
    """<p>Encryption options for a package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageDetails) -> dict:
    out: dict = {}
    if "package_id" in value:
        out["PackageID"] = value["package_id"]
    if "package_name" in value:
        out["PackageName"] = value["package_name"]
    if "package_type" in value:
        import aws_sdk_opensearch.types.package_type

        out["PackageType"] = aws_sdk_opensearch.types.package_type.serialize_json(
            value["package_type"]
        )
    if "package_description" in value:
        out["PackageDescription"] = value["package_description"]
    if "package_status" in value:
        import aws_sdk_opensearch.types.package_status

        out["PackageStatus"] = aws_sdk_opensearch.types.package_status.serialize_json(
            value["package_status"]
        )
    if "created_at" in value:
        import aws_sdk_opensearch.types.created_at

        out["CreatedAt"] = aws_sdk_opensearch.types.created_at.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_opensearch.types.last_updated

        out["LastUpdatedAt"] = aws_sdk_opensearch.types.last_updated.serialize_json(
            value["last_updated_at"]
        )
    if "available_package_version" in value:
        out["AvailablePackageVersion"] = value["available_package_version"]
    if "error_details" in value:
        import aws_sdk_opensearch.types.error_details

        out["ErrorDetails"] = aws_sdk_opensearch.types.error_details.serialize_json(
            value["error_details"]
        )
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "available_plugin_properties" in value:
        import aws_sdk_opensearch.types.plugin_properties

        out["AvailablePluginProperties"] = (
            aws_sdk_opensearch.types.plugin_properties.serialize_json(
                value["available_plugin_properties"]
            )
        )
    if "available_package_configuration" in value:
        import aws_sdk_opensearch.types.package_configuration

        out["AvailablePackageConfiguration"] = (
            aws_sdk_opensearch.types.package_configuration.serialize_json(
                value["available_package_configuration"]
            )
        )
    if "allow_listed_user_list" in value:
        import aws_sdk_opensearch.types.package_user_list

        out["AllowListedUserList"] = (
            aws_sdk_opensearch.types.package_user_list.serialize_json(
                value["allow_listed_user_list"]
            )
        )
    if "package_owner" in value:
        out["PackageOwner"] = value["package_owner"]
    if "package_vending_options" in value:
        import aws_sdk_opensearch.types.package_vending_options

        out["PackageVendingOptions"] = (
            aws_sdk_opensearch.types.package_vending_options.serialize_json(
                value["package_vending_options"]
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


def deserialize_json(data: dict) -> PackageDetails:
    out: PackageDetails = {}  # type: ignore[typeddict-item]
    if "PackageID" in data:
        out["package_id"] = data["PackageID"]
    if "PackageName" in data:
        out["package_name"] = data["PackageName"]
    if "PackageType" in data:
        import aws_sdk_opensearch.types.package_type

        out["package_type"] = aws_sdk_opensearch.types.package_type.deserialize_json(
            data["PackageType"]
        )
    if "PackageDescription" in data:
        out["package_description"] = data["PackageDescription"]
    if "PackageStatus" in data:
        import aws_sdk_opensearch.types.package_status

        out["package_status"] = (
            aws_sdk_opensearch.types.package_status.deserialize_json(
                data["PackageStatus"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_opensearch.types.created_at

        out["created_at"] = aws_sdk_opensearch.types.created_at.deserialize_json(
            data["CreatedAt"]
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_opensearch.types.last_updated

        out["last_updated_at"] = aws_sdk_opensearch.types.last_updated.deserialize_json(
            data["LastUpdatedAt"]
        )
    if "AvailablePackageVersion" in data:
        out["available_package_version"] = data["AvailablePackageVersion"]
    if "ErrorDetails" in data:
        import aws_sdk_opensearch.types.error_details

        out["error_details"] = aws_sdk_opensearch.types.error_details.deserialize_json(
            data["ErrorDetails"]
        )
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "AvailablePluginProperties" in data:
        import aws_sdk_opensearch.types.plugin_properties

        out["available_plugin_properties"] = (
            aws_sdk_opensearch.types.plugin_properties.deserialize_json(
                data["AvailablePluginProperties"]
            )
        )
    if "AvailablePackageConfiguration" in data:
        import aws_sdk_opensearch.types.package_configuration

        out["available_package_configuration"] = (
            aws_sdk_opensearch.types.package_configuration.deserialize_json(
                data["AvailablePackageConfiguration"]
            )
        )
    if "AllowListedUserList" in data:
        import aws_sdk_opensearch.types.package_user_list

        out["allow_listed_user_list"] = (
            aws_sdk_opensearch.types.package_user_list.deserialize_json(
                data["AllowListedUserList"]
            )
        )
    if "PackageOwner" in data:
        out["package_owner"] = data["PackageOwner"]
    if "PackageVendingOptions" in data:
        import aws_sdk_opensearch.types.package_vending_options

        out["package_vending_options"] = (
            aws_sdk_opensearch.types.package_vending_options.deserialize_json(
                data["PackageVendingOptions"]
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
