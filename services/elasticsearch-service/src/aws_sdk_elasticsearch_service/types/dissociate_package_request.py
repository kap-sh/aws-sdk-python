"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DissociatePackageRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_name
    import aws_sdk_elasticsearch_service.types.package_id


class DissociatePackageRequest(TypedDict):
    package_id: "aws_sdk_elasticsearch_service.types.package_id.PackageID"
    """<p>Internal ID of the package that you want to associate with a domain. Use <code>DescribePackages</code> to find this value.</p>"""
    domain_name: "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    """<p>Name of the domain that you want to associate the package with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DissociatePackageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DissociatePackageRequest:
    out: DissociatePackageRequest = {}  # type: ignore[typeddict-item]
    return out
