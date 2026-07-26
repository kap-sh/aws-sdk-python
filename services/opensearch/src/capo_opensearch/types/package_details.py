"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.created_at
    import capo_opensearch.types.engine_version
    import capo_opensearch.types.error_details
    import capo_opensearch.types.last_updated
    import capo_opensearch.types.package_configuration
    import capo_opensearch.types.package_description
    import capo_opensearch.types.package_encryption_options
    import capo_opensearch.types.package_id
    import capo_opensearch.types.package_name
    import capo_opensearch.types.package_owner
    import capo_opensearch.types.package_status
    import capo_opensearch.types.package_type
    import capo_opensearch.types.package_user_list
    import capo_opensearch.types.package_vending_options
    import capo_opensearch.types.package_version
    import capo_opensearch.types.plugin_properties


class PackageDetails(TypedDict, closed=True):
    package_id: NotRequired["capo_opensearch.types.package_id.PackageID"]
    """<p>The unique identifier of the package.</p>"""
    package_name: NotRequired["capo_opensearch.types.package_name.PackageName"]
    """<p>The user-specified name of the package.</p>"""
    package_type: NotRequired["capo_opensearch.types.package_type.PackageType"]
    """<p>The type of package.</p>"""
    package_description: NotRequired[
        "capo_opensearch.types.package_description.PackageDescription"
    ]
    """<p>User-specified description of the package.</p>"""
    package_status: NotRequired["capo_opensearch.types.package_status.PackageStatus"]
    """<p>The current status of the package. The available options are <code>AVAILABLE</code>, <code>COPYING</code>, <code>COPY_FAILED</code>, <code>VALIDATNG</code>, <code>VALIDATION_FAILED</code>, <code>DELETING</code>, and <code>DELETE_FAILED</code>.</p>"""
    created_at: NotRequired["capo_opensearch.types.created_at.CreatedAt"]
    """<p>The timestamp when the package was created.</p>"""
    last_updated_at: NotRequired["capo_opensearch.types.last_updated.LastUpdated"]
    """<p>Date and time when the package was last updated.</p>"""
    available_package_version: NotRequired[
        "capo_opensearch.types.package_version.PackageVersion"
    ]
    """<p>The package version.</p>"""
    error_details: NotRequired["capo_opensearch.types.error_details.ErrorDetails"]
    """<p>Additional information if the package is in an error state. Null otherwise.</p>"""
    engine_version: NotRequired["capo_opensearch.types.engine_version.EngineVersion"]
    """<p>Version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch.</p>"""
    available_plugin_properties: NotRequired[
        "capo_opensearch.types.plugin_properties.PluginProperties"
    ]
    """<p>If the package is a <code>ZIP-PLUGIN</code> package, additional information about plugin properties.</p>"""
    available_package_configuration: NotRequired[
        "capo_opensearch.types.package_configuration.PackageConfiguration"
    ]
    """<p>This represents the available configuration parameters for the package.</p>"""
    allow_listed_user_list: NotRequired[
        "capo_opensearch.types.package_user_list.PackageUserList"
    ]
    """<p> A list of users who are allowed to view and associate the package. This field is only visible to the owner of a package.</p>"""
    package_owner: NotRequired["capo_opensearch.types.package_owner.PackageOwner"]
    """<p>The owner of the package who is allowed to create and update a package and add users to the package scope.</p>"""
    package_vending_options: NotRequired[
        "capo_opensearch.types.package_vending_options.PackageVendingOptions"
    ]
    """<p>Package Vending Options for a package.</p>"""
    package_encryption_options: NotRequired[
        "capo_opensearch.types.package_encryption_options.PackageEncryptionOptions"
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
        import capo_opensearch.types.package_type

        out["PackageType"] = capo_opensearch.types.package_type.serialize_json(
            value["package_type"]
        )
    if "package_description" in value:
        out["PackageDescription"] = value["package_description"]
    if "package_status" in value:
        import capo_opensearch.types.package_status

        out["PackageStatus"] = capo_opensearch.types.package_status.serialize_json(
            value["package_status"]
        )
    if "created_at" in value:
        import capo_opensearch.types.created_at

        out["CreatedAt"] = capo_opensearch.types.created_at.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_opensearch.types.last_updated

        out["LastUpdatedAt"] = capo_opensearch.types.last_updated.serialize_json(
            value["last_updated_at"]
        )
    if "available_package_version" in value:
        out["AvailablePackageVersion"] = value["available_package_version"]
    if "error_details" in value:
        import capo_opensearch.types.error_details

        out["ErrorDetails"] = capo_opensearch.types.error_details.serialize_json(
            value["error_details"]
        )
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "available_plugin_properties" in value:
        import capo_opensearch.types.plugin_properties

        out["AvailablePluginProperties"] = (
            capo_opensearch.types.plugin_properties.serialize_json(
                value["available_plugin_properties"]
            )
        )
    if "available_package_configuration" in value:
        import capo_opensearch.types.package_configuration

        out["AvailablePackageConfiguration"] = (
            capo_opensearch.types.package_configuration.serialize_json(
                value["available_package_configuration"]
            )
        )
    if "allow_listed_user_list" in value:
        import capo_opensearch.types.package_user_list

        out["AllowListedUserList"] = (
            capo_opensearch.types.package_user_list.serialize_json(
                value["allow_listed_user_list"]
            )
        )
    if "package_owner" in value:
        out["PackageOwner"] = value["package_owner"]
    if "package_vending_options" in value:
        import capo_opensearch.types.package_vending_options

        out["PackageVendingOptions"] = (
            capo_opensearch.types.package_vending_options.serialize_json(
                value["package_vending_options"]
            )
        )
    if "package_encryption_options" in value:
        import capo_opensearch.types.package_encryption_options

        out["PackageEncryptionOptions"] = (
            capo_opensearch.types.package_encryption_options.serialize_json(
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
        import capo_opensearch.types.package_type

        out["package_type"] = capo_opensearch.types.package_type.deserialize_json(
            data["PackageType"]
        )
    if "PackageDescription" in data:
        out["package_description"] = data["PackageDescription"]
    if "PackageStatus" in data:
        import capo_opensearch.types.package_status

        out["package_status"] = capo_opensearch.types.package_status.deserialize_json(
            data["PackageStatus"]
        )
    if "CreatedAt" in data:
        import capo_opensearch.types.created_at

        out["created_at"] = capo_opensearch.types.created_at.deserialize_json(
            data["CreatedAt"]
        )
    if "LastUpdatedAt" in data:
        import capo_opensearch.types.last_updated

        out["last_updated_at"] = capo_opensearch.types.last_updated.deserialize_json(
            data["LastUpdatedAt"]
        )
    if "AvailablePackageVersion" in data:
        out["available_package_version"] = data["AvailablePackageVersion"]
    if "ErrorDetails" in data:
        import capo_opensearch.types.error_details

        out["error_details"] = capo_opensearch.types.error_details.deserialize_json(
            data["ErrorDetails"]
        )
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "AvailablePluginProperties" in data:
        import capo_opensearch.types.plugin_properties

        out["available_plugin_properties"] = (
            capo_opensearch.types.plugin_properties.deserialize_json(
                data["AvailablePluginProperties"]
            )
        )
    if "AvailablePackageConfiguration" in data:
        import capo_opensearch.types.package_configuration

        out["available_package_configuration"] = (
            capo_opensearch.types.package_configuration.deserialize_json(
                data["AvailablePackageConfiguration"]
            )
        )
    if "AllowListedUserList" in data:
        import capo_opensearch.types.package_user_list

        out["allow_listed_user_list"] = (
            capo_opensearch.types.package_user_list.deserialize_json(
                data["AllowListedUserList"]
            )
        )
    if "PackageOwner" in data:
        out["package_owner"] = data["PackageOwner"]
    if "PackageVendingOptions" in data:
        import capo_opensearch.types.package_vending_options

        out["package_vending_options"] = (
            capo_opensearch.types.package_vending_options.deserialize_json(
                data["PackageVendingOptions"]
            )
        )
    if "PackageEncryptionOptions" in data:
        import capo_opensearch.types.package_encryption_options

        out["package_encryption_options"] = (
            capo_opensearch.types.package_encryption_options.deserialize_json(
                data["PackageEncryptionOptions"]
            )
        )
    return out
