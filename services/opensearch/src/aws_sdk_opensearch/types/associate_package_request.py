"""Generated from Smithy shape ``com.amazonaws.opensearch#AssociatePackageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.package_association_configuration
    import aws_sdk_opensearch.types.package_id
    import aws_sdk_opensearch.types.package_id_list


class AssociatePackageRequest(TypedDict, closed=True):
    package_id: "aws_sdk_opensearch.types.package_id.PackageID"
    """<p>Internal ID of the package to associate with a domain. Use <code>DescribePackages</code> to find this value. </p>"""
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>Name of the domain to associate the package with.</p>"""
    prerequisite_package_id_list: NotRequired[
        "aws_sdk_opensearch.types.package_id_list.PackageIDList"
    ]
    """<p>A list of package IDs that must be associated with the domain before the package specified in the request can be associated.</p>"""
    association_configuration: NotRequired[
        "aws_sdk_opensearch.types.package_association_configuration.PackageAssociationConfiguration"
    ]
    """<p>The configuration for associating a package with an Amazon OpenSearch Service domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatePackageRequest) -> dict:
    out: dict = {}
    if "prerequisite_package_id_list" in value:
        import aws_sdk_opensearch.types.package_id_list

        out["PrerequisitePackageIDList"] = (
            aws_sdk_opensearch.types.package_id_list.serialize_json(
                value["prerequisite_package_id_list"]
            )
        )
    if "association_configuration" in value:
        import aws_sdk_opensearch.types.package_association_configuration

        out["AssociationConfiguration"] = (
            aws_sdk_opensearch.types.package_association_configuration.serialize_json(
                value["association_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociatePackageRequest:
    out: AssociatePackageRequest = {}  # type: ignore[typeddict-item]
    if "PrerequisitePackageIDList" in data:
        import aws_sdk_opensearch.types.package_id_list

        out["prerequisite_package_id_list"] = (
            aws_sdk_opensearch.types.package_id_list.deserialize_json(
                data["PrerequisitePackageIDList"]
            )
        )
    if "AssociationConfiguration" in data:
        import aws_sdk_opensearch.types.package_association_configuration

        out["association_configuration"] = (
            aws_sdk_opensearch.types.package_association_configuration.deserialize_json(
                data["AssociationConfiguration"]
            )
        )
    return out
