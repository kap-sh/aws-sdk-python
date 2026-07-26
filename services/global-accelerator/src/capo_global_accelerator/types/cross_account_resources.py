"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CrossAccountResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.cross_account_resource

CrossAccountResources: TypeAlias = list[
    "capo_global_accelerator.types.cross_account_resource.CrossAccountResource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrossAccountResources) -> list:
    import capo_global_accelerator.types.cross_account_resource

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.cross_account_resource.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CrossAccountResources:
    import capo_global_accelerator.types.cross_account_resource

    out: CrossAccountResources = []
    for item in data:
        out.append(
            capo_global_accelerator.types.cross_account_resource.deserialize_aws_json_1_1(
                item
            )
        )
    return out
