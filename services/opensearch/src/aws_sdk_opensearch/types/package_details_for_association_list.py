"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageDetailsForAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.package_details_for_association

PackageDetailsForAssociationList: TypeAlias = list[
    "aws_sdk_opensearch.types.package_details_for_association.PackageDetailsForAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageDetailsForAssociationList) -> list:
    import aws_sdk_opensearch.types.package_details_for_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_opensearch.types.package_details_for_association.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PackageDetailsForAssociationList:
    import aws_sdk_opensearch.types.package_details_for_association

    out: PackageDetailsForAssociationList = []
    for item in data:
        out.append(
            aws_sdk_opensearch.types.package_details_for_association.deserialize_json(
                item
            )
        )
    return out
