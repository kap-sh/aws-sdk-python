"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.package_details

PackageDetailsList: TypeAlias = list[
    "capo_opensearch.types.package_details.PackageDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageDetailsList) -> list:
    import capo_opensearch.types.package_details

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.package_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> PackageDetailsList:
    import capo_opensearch.types.package_details

    out: PackageDetailsList = []
    for item in data:
        out.append(capo_opensearch.types.package_details.deserialize_json(item))
    return out
