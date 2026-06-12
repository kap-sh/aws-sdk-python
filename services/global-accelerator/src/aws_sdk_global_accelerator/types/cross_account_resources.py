"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CrossAccountResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.cross_account_resource

CrossAccountResources: TypeAlias = list[
    "aws_sdk_global_accelerator.types.cross_account_resource.CrossAccountResource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrossAccountResources) -> list:
    import aws_sdk_global_accelerator.types.cross_account_resource

    out: list = []
    for item in value:
        out.append(
            aws_sdk_global_accelerator.types.cross_account_resource.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CrossAccountResources:
    import aws_sdk_global_accelerator.types.cross_account_resource

    out: CrossAccountResources = []
    for item in data:
        out.append(
            aws_sdk_global_accelerator.types.cross_account_resource.deserialize_aws_json_1_1(
                item
            )
        )
    return out
