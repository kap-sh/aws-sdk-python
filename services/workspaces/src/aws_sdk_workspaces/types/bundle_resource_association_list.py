"""Generated from Smithy shape ``com.amazonaws.workspaces#BundleResourceAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.bundle_resource_association

BundleResourceAssociationList: TypeAlias = list[
    "aws_sdk_workspaces.types.bundle_resource_association.BundleResourceAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BundleResourceAssociationList) -> list:
    import aws_sdk_workspaces.types.bundle_resource_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.bundle_resource_association.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BundleResourceAssociationList:
    import aws_sdk_workspaces.types.bundle_resource_association

    out: BundleResourceAssociationList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.bundle_resource_association.deserialize_aws_json_1_1(
                item
            )
        )
    return out
