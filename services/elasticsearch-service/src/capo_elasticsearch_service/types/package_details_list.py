"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#PackageDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.package_details

PackageDetailsList: TypeAlias = list[
    "capo_elasticsearch_service.types.package_details.PackageDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageDetailsList) -> list:
    import capo_elasticsearch_service.types.package_details

    out: list = []
    for item in value:
        out.append(
            capo_elasticsearch_service.types.package_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PackageDetailsList:
    import capo_elasticsearch_service.types.package_details

    out: PackageDetailsList = []
    for item in data:
        out.append(
            capo_elasticsearch_service.types.package_details.deserialize_json(item)
        )
    return out
