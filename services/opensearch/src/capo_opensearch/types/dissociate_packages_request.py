"""Generated from Smithy shape ``com.amazonaws.opensearch#DissociatePackagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.package_id_list


class DissociatePackagesRequest(TypedDict, closed=True):
    package_list: "capo_opensearch.types.package_id_list.PackageIDList"
    """<p>A list of package IDs to be dissociated from a domain.</p>"""
    domain_name: "capo_opensearch.types.domain_name.DomainName"


# --- restJson1 ser/de ---
def serialize_json(value: DissociatePackagesRequest) -> dict:
    out: dict = {}
    import capo_opensearch.types.package_id_list

    out["PackageList"] = capo_opensearch.types.package_id_list.serialize_json(
        value["package_list"]
    )
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_json(data: dict) -> DissociatePackagesRequest:
    out: DissociatePackagesRequest = {}  # type: ignore[typeddict-item]
    if "PackageList" in data:
        import capo_opensearch.types.package_id_list

        out["package_list"] = capo_opensearch.types.package_id_list.deserialize_json(
            data["PackageList"]
        )
    else:
        raise DeserializationError("DissociatePackagesRequest.package_list required")
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("DissociatePackagesRequest.domain_name required")
    return out
