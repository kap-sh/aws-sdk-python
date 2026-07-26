"""Generated from Smithy shape ``com.amazonaws.workspaces#BundleAssociatedResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.bundle_associated_resource_type

BundleAssociatedResourceTypeList: TypeAlias = list[
    "capo_workspaces.types.bundle_associated_resource_type.BundleAssociatedResourceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BundleAssociatedResourceTypeList) -> list:
    import capo_workspaces.types.bundle_associated_resource_type

    out: list = []
    for item in value:
        out.append(
            capo_workspaces.types.bundle_associated_resource_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BundleAssociatedResourceTypeList:
    import capo_workspaces.types.bundle_associated_resource_type

    out: BundleAssociatedResourceTypeList = []
    for item in data:
        out.append(
            capo_workspaces.types.bundle_associated_resource_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
