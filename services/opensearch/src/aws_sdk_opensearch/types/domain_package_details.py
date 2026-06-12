"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainPackageDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.domain_package_status
    import aws_sdk_opensearch.types.error_details
    import aws_sdk_opensearch.types.last_updated
    import aws_sdk_opensearch.types.package_association_configuration
    import aws_sdk_opensearch.types.package_id
    import aws_sdk_opensearch.types.package_id_list
    import aws_sdk_opensearch.types.package_name
    import aws_sdk_opensearch.types.package_type
    import aws_sdk_opensearch.types.package_version
    import aws_sdk_opensearch.types.reference_path


class DomainPackageDetails(TypedDict):
    package_id: NotRequired["aws_sdk_opensearch.types.package_id.PackageID"]
    """<p>Internal ID of the package.</p>"""
    package_name: NotRequired["aws_sdk_opensearch.types.package_name.PackageName"]
    """<p>User-specified name of the package.</p>"""
    package_type: NotRequired["aws_sdk_opensearch.types.package_type.PackageType"]
    """<p>The type of package.</p>"""
    last_updated: NotRequired["aws_sdk_opensearch.types.last_updated.LastUpdated"]
    """<p>Timestamp of the most recent update to the package association status.</p>"""
    domain_name: NotRequired["aws_sdk_opensearch.types.domain_name.DomainName"]
    """<p>Name of the domain that the package is associated with.</p>"""
    domain_package_status: NotRequired[
        "aws_sdk_opensearch.types.domain_package_status.DomainPackageStatus"
    ]
    """<p>State of the association.</p>"""
    package_version: NotRequired[
        "aws_sdk_opensearch.types.package_version.PackageVersion"
    ]
    """<p>The current version of the package.</p>"""
    prerequisite_package_id_list: NotRequired[
        "aws_sdk_opensearch.types.package_id_list.PackageIDList"
    ]
    """<p>A list of package IDs that must be associated with the domain before or with the package can be associated.</p>"""
    reference_path: NotRequired["aws_sdk_opensearch.types.reference_path.ReferencePath"]
    """<p>The relative path of the package on the OpenSearch Service cluster nodes. This is <code>synonym_path</code> when the package is for synonym files.</p>"""
    error_details: NotRequired["aws_sdk_opensearch.types.error_details.ErrorDetails"]
    """<p>Additional information if the package is in an error state. Null otherwise.</p>"""
    association_configuration: NotRequired[
        "aws_sdk_opensearch.types.package_association_configuration.PackageAssociationConfiguration"
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
        import aws_sdk_opensearch.types.package_type

        out["PackageType"] = aws_sdk_opensearch.types.package_type.serialize_json(
            value["package_type"]
        )
    if "last_updated" in value:
        import aws_sdk_opensearch.types.last_updated

        out["LastUpdated"] = aws_sdk_opensearch.types.last_updated.serialize_json(
            value["last_updated"]
        )
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "domain_package_status" in value:
        import aws_sdk_opensearch.types.domain_package_status

        out["DomainPackageStatus"] = (
            aws_sdk_opensearch.types.domain_package_status.serialize_json(
                value["domain_package_status"]
            )
        )
    if "package_version" in value:
        out["PackageVersion"] = value["package_version"]
    if "prerequisite_package_id_list" in value:
        import aws_sdk_opensearch.types.package_id_list

        out["PrerequisitePackageIDList"] = (
            aws_sdk_opensearch.types.package_id_list.serialize_json(
                value["prerequisite_package_id_list"]
            )
        )
    if "reference_path" in value:
        out["ReferencePath"] = value["reference_path"]
    if "error_details" in value:
        import aws_sdk_opensearch.types.error_details

        out["ErrorDetails"] = aws_sdk_opensearch.types.error_details.serialize_json(
            value["error_details"]
        )
    if "association_configuration" in value:
        import aws_sdk_opensearch.types.package_association_configuration

        out["AssociationConfiguration"] = (
            aws_sdk_opensearch.types.package_association_configuration.serialize_json(
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
        import aws_sdk_opensearch.types.package_type

        out["package_type"] = aws_sdk_opensearch.types.package_type.deserialize_json(
            data["PackageType"]
        )
    if "LastUpdated" in data:
        import aws_sdk_opensearch.types.last_updated

        out["last_updated"] = aws_sdk_opensearch.types.last_updated.deserialize_json(
            data["LastUpdated"]
        )
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "DomainPackageStatus" in data:
        import aws_sdk_opensearch.types.domain_package_status

        out["domain_package_status"] = (
            aws_sdk_opensearch.types.domain_package_status.deserialize_json(
                data["DomainPackageStatus"]
            )
        )
    if "PackageVersion" in data:
        out["package_version"] = data["PackageVersion"]
    if "PrerequisitePackageIDList" in data:
        import aws_sdk_opensearch.types.package_id_list

        out["prerequisite_package_id_list"] = (
            aws_sdk_opensearch.types.package_id_list.deserialize_json(
                data["PrerequisitePackageIDList"]
            )
        )
    if "ReferencePath" in data:
        out["reference_path"] = data["ReferencePath"]
    if "ErrorDetails" in data:
        import aws_sdk_opensearch.types.error_details

        out["error_details"] = aws_sdk_opensearch.types.error_details.deserialize_json(
            data["ErrorDetails"]
        )
    if "AssociationConfiguration" in data:
        import aws_sdk_opensearch.types.package_association_configuration

        out["association_configuration"] = (
            aws_sdk_opensearch.types.package_association_configuration.deserialize_json(
                data["AssociationConfiguration"]
            )
        )
    return out
