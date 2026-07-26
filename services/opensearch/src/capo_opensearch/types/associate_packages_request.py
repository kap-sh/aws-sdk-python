"""Generated from Smithy shape ``com.amazonaws.opensearch#AssociatePackagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.package_details_for_association_list


class AssociatePackagesRequest(TypedDict, closed=True):
    package_list: "capo_opensearch.types.package_details_for_association_list.PackageDetailsForAssociationList"
    """<p>A list of packages and their prerequisites to be associated with a domain.</p>"""
    domain_name: "capo_opensearch.types.domain_name.DomainName"


# --- restJson1 ser/de ---
def serialize_json(value: AssociatePackagesRequest) -> dict:
    out: dict = {}
    import capo_opensearch.types.package_details_for_association_list

    out["PackageList"] = (
        capo_opensearch.types.package_details_for_association_list.serialize_json(
            value["package_list"]
        )
    )
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_json(data: dict) -> AssociatePackagesRequest:
    out: AssociatePackagesRequest = {}  # type: ignore[typeddict-item]
    if "PackageList" in data:
        import capo_opensearch.types.package_details_for_association_list

        out["package_list"] = (
            capo_opensearch.types.package_details_for_association_list.deserialize_json(
                data["PackageList"]
            )
        )
    else:
        raise DeserializationError("AssociatePackagesRequest.package_list required")
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("AssociatePackagesRequest.domain_name required")
    return out
