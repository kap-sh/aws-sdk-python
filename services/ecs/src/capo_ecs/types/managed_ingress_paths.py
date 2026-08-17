"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedIngressPaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.managed_ingress_path

ManagedIngressPaths: TypeAlias = list[
    "capo_ecs.types.managed_ingress_path.ManagedIngressPath"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedIngressPaths) -> list:
    import capo_ecs.types.managed_ingress_path

    out: list = []
    for item in value:
        out.append(capo_ecs.types.managed_ingress_path.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedIngressPaths:
    import capo_ecs.types.managed_ingress_path

    out: ManagedIngressPaths = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.managed_ingress_path.deserialize_aws_json_1_1(item))
    return out
