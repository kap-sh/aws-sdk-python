"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainPackageDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.domain_package_status
    import capo_opensearch.types.error_details
    import capo_opensearch.types.last_updated
    import capo_opensearch.types.package_association_configuration
    import capo_opensearch.types.package_id
    import capo_opensearch.types.package_id_list
    import capo_opensearch.types.package_name
    import capo_opensearch.types.package_type
    import capo_opensearch.types.package_version
    import capo_opensearch.types.reference_path


class DomainPackageDetails(TypedDict, closed=True):
    package_id: NotRequired["capo_opensearch.types.package_id.PackageID"]
    """<p>Internal ID of the package.</p>"""
    package_name: NotRequired["capo_opensearch.types.package_name.PackageName"]
    """<p>User-specified name of the package.</p>"""
    package_type: NotRequired["capo_opensearch.types.package_type.PackageType"]
    """<p>The type of package.</p>"""
    last_updated: NotRequired["capo_opensearch.types.last_updated.LastUpdated"]
    """<p>Timestamp of the most recent update to the package association status.</p>"""
    domain_name: NotRequired["capo_opensearch.types.domain_name.DomainName"]
    """<p>Name of the domain that the package is associated with.</p>"""
    domain_package_status: NotRequired[
        "capo_opensearch.types.domain_package_status.DomainPackageStatus"
    ]
    """<p>State of the association.</p>"""
    package_version: NotRequired["capo_opensearch.types.package_version.PackageVersion"]
    """<p>The current version of the package.</p>"""
    prerequisite_package_id_list: NotRequired[
        "capo_opensearch.types.package_id_list.PackageIDList"
    ]
    """<p>A list of package IDs that must be associated with the domain before or with the package can be associated.</p>"""
    reference_path: NotRequired["capo_opensearch.types.reference_path.ReferencePath"]
    """<p>The relative path of the package on the OpenSearch Service cluster nodes. This is <code>synonym_path</code> when the package is for synonym files.</p>"""
    error_details: NotRequired["capo_opensearch.types.error_details.ErrorDetails"]
    """<p>Additional information if the package is in an error state. Null otherwise.</p>"""
    association_configuration: NotRequired[
        "capo_opensearch.types.package_association_configuration.PackageAssociationConfiguration"
    ]
    """<p>The configuration for associating a package with an Amazon OpenSearch Service domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainPackageDetails) -> dict:
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
    if "last_updated" in value:
        import capo_opensearch.types.last_updated

        out["LastUpdated"] = capo_opensearch.types.last_updated.serialize_json(
            value["last_updated"]
        )
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "domain_package_status" in value:
        import capo_opensearch.types.domain_package_status

        out["DomainPackageStatus"] = (
            capo_opensearch.types.domain_package_status.serialize_json(
                value["domain_package_status"]
            )
        )
    if "package_version" in value:
        out["PackageVersion"] = value["package_version"]
    if "prerequisite_package_id_list" in value:
        import capo_opensearch.types.package_id_list

        out["PrerequisitePackageIDList"] = (
            capo_opensearch.types.package_id_list.serialize_json(
                value["prerequisite_package_id_list"]
            )
        )
    if "reference_path" in value:
        out["ReferencePath"] = value["reference_path"]
    if "error_details" in value:
        import capo_opensearch.types.error_details

        out["ErrorDetails"] = capo_opensearch.types.error_details.serialize_json(
            value["error_details"]
        )
    if "association_configuration" in value:
        import capo_opensearch.types.package_association_configuration

        out["AssociationConfiguration"] = (
            capo_opensearch.types.package_association_configuration.serialize_json(
                value["association_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DomainPackageDetails:
    out: DomainPackageDetails = {}  # type: ignore[typeddict-item]
    if "PackageID" in data:
        out["package_id"] = data["PackageID"]
    if "PackageName" in data:
        out["package_name"] = data["PackageName"]
    if "PackageType" in data:
        import capo_opensearch.types.package_type

        out["package_type"] = capo_opensearch.types.package_type.deserialize_json(
            data["PackageType"]
        )
    if "LastUpdated" in data:
        import capo_opensearch.types.last_updated

        out["last_updated"] = capo_opensearch.types.last_updated.deserialize_json(
            data["LastUpdated"]
        )
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "DomainPackageStatus" in data:
        import capo_opensearch.types.domain_package_status

        out["domain_package_status"] = (
            capo_opensearch.types.domain_package_status.deserialize_json(
                data["DomainPackageStatus"]
            )
        )
    if "PackageVersion" in data:
        out["package_version"] = data["PackageVersion"]
    if "PrerequisitePackageIDList" in data:
        import capo_opensearch.types.package_id_list

        out["prerequisite_package_id_list"] = (
            capo_opensearch.types.package_id_list.deserialize_json(
                data["PrerequisitePackageIDList"]
            )
        )
    if "ReferencePath" in data:
        out["reference_path"] = data["ReferencePath"]
    if "ErrorDetails" in data:
        import capo_opensearch.types.error_details

        out["error_details"] = capo_opensearch.types.error_details.deserialize_json(
            data["ErrorDetails"]
        )
    if "AssociationConfiguration" in data:
        import capo_opensearch.types.package_association_configuration

        out["association_configuration"] = (
            capo_opensearch.types.package_association_configuration.deserialize_json(
                data["AssociationConfiguration"]
            )
        )
    return out
