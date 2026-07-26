"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageDetailsForAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.package_details_for_association

PackageDetailsForAssociationList: TypeAlias = list[
    "capo_opensearch.types.package_details_for_association.PackageDetailsForAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageDetailsForAssociationList) -> list:
    import capo_opensearch.types.package_details_for_association

    out: list = []
    for item in value:
        out.append(
            capo_opensearch.types.package_details_for_association.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PackageDetailsForAssociationList:
    import capo_opensearch.types.package_details_for_association

    out: PackageDetailsForAssociationList = []
    for item in data:
        out.append(
            capo_opensearch.types.package_details_for_association.deserialize_json(item)
        )
    return out
