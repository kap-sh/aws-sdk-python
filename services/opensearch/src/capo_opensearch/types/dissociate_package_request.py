"""Generated from Smithy shape ``com.amazonaws.opensearch#DissociatePackageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name
    import capo_opensearch.types.package_id


class DissociatePackageRequest(TypedDict, closed=True):
    package_id: "capo_opensearch.types.package_id.PackageID"
    """<p>Internal ID of the package to dissociate from the domain. Use <code>ListPackagesForDomain</code> to find this value.</p>"""
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>Name of the domain to dissociate the package from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DissociatePackageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DissociatePackageRequest:
    out: DissociatePackageRequest = {}  # type: ignore[typeddict-item]
    return out
