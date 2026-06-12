"""Generated from Smithy shape ``com.amazonaws.opensearch#DissociatePackageRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.package_id


class DissociatePackageRequest(TypedDict):
    package_id: "aws_sdk_opensearch.types.package_id.PackageID"
    """<p>Internal ID of the package to dissociate from the domain. Use <code>ListPackagesForDomain</code> to find this value.</p>"""
    domain_name: "aws_sdk_opensearch.types.domain_name.DomainName"
    """<p>Name of the domain to dissociate the package from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DissociatePackageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DissociatePackageRequest:
    out: DissociatePackageRequest = {}  # type: ignore[typeddict-item]
    return out
