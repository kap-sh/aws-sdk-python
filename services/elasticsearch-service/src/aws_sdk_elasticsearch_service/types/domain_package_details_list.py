"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DomainPackageDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_package_details

DomainPackageDetailsList: TypeAlias = list[
    "aws_sdk_elasticsearch_service.types.domain_package_details.DomainPackageDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainPackageDetailsList) -> list:
    import aws_sdk_elasticsearch_service.types.domain_package_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_elasticsearch_service.types.domain_package_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DomainPackageDetailsList:
    import aws_sdk_elasticsearch_service.types.domain_package_details

    out: DomainPackageDetailsList = []
    for item in data:
        out.append(
            aws_sdk_elasticsearch_service.types.domain_package_details.deserialize_json(
                item
            )
        )
    return out
