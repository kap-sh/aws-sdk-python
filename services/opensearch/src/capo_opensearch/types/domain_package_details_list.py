"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainPackageDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.domain_package_details

DomainPackageDetailsList: TypeAlias = list[
    "capo_opensearch.types.domain_package_details.DomainPackageDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainPackageDetailsList) -> list:
    import capo_opensearch.types.domain_package_details

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.domain_package_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainPackageDetailsList:
    import capo_opensearch.types.domain_package_details

    out: DomainPackageDetailsList = []
    for item in data:
        out.append(capo_opensearch.types.domain_package_details.deserialize_json(item))
    return out
