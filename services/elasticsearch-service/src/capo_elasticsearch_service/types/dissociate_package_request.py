"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DissociatePackageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_name
    import capo_elasticsearch_service.types.package_id


class DissociatePackageRequest(TypedDict, closed=True):
    package_id: "capo_elasticsearch_service.types.package_id.PackageID"
    """<p>Internal ID of the package that you want to associate with a domain. Use <code>DescribePackages</code> to find this value.</p>"""
    domain_name: "capo_elasticsearch_service.types.domain_name.DomainName"
    """<p>Name of the domain that you want to associate the package with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DissociatePackageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DissociatePackageRequest:
    out: DissociatePackageRequest = {}  # type: ignore[typeddict-item]
    return out
