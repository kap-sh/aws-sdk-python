"""Generated from Smithy shape ``com.amazonaws.workspaces#BundleAssociatedResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.bundle_associated_resource_type

BundleAssociatedResourceTypeList: TypeAlias = list[
    "aws_sdk_workspaces.types.bundle_associated_resource_type.BundleAssociatedResourceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BundleAssociatedResourceTypeList) -> list:
    import aws_sdk_workspaces.types.bundle_associated_resource_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.bundle_associated_resource_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BundleAssociatedResourceTypeList:
    import aws_sdk_workspaces.types.bundle_associated_resource_type

    out: BundleAssociatedResourceTypeList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.bundle_associated_resource_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
