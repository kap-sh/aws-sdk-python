"""Generated from Smithy shape ``com.amazonaws.devopsguru#ServiceResourceCosts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.service_resource_cost

ServiceResourceCosts: TypeAlias = list[
    "aws_sdk_devops_guru.types.service_resource_cost.ServiceResourceCost"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceResourceCosts) -> list:
    import aws_sdk_devops_guru.types.service_resource_cost

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_guru.types.service_resource_cost.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceResourceCosts:
    import aws_sdk_devops_guru.types.service_resource_cost

    out: ServiceResourceCosts = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.service_resource_cost.deserialize_json(item)
        )
    return out
