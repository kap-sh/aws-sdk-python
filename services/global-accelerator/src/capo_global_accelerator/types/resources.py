"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#Resources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.resource

Resources: TypeAlias = list["capo_global_accelerator.types.resource.Resource"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Resources) -> list:
    import capo_global_accelerator.types.resource

    out: list = []
    for item in value:
        out.append(capo_global_accelerator.types.resource.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Resources:
    import capo_global_accelerator.types.resource

    out: Resources = []
    for item in data:
        out.append(
            capo_global_accelerator.types.resource.deserialize_aws_json_1_1(item)
        )
    return out
