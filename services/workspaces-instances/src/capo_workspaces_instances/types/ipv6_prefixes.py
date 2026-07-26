"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#Ipv6Prefixes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.ipv6_prefix_specification_request

Ipv6Prefixes: TypeAlias = list[
    "capo_workspaces_instances.types.ipv6_prefix_specification_request.Ipv6PrefixSpecificationRequest"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ipv6Prefixes) -> list:
    import capo_workspaces_instances.types.ipv6_prefix_specification_request

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.ipv6_prefix_specification_request.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Ipv6Prefixes:
    import capo_workspaces_instances.types.ipv6_prefix_specification_request

    out: Ipv6Prefixes = []
    for item in data:
        out.append(
            capo_workspaces_instances.types.ipv6_prefix_specification_request.deserialize_aws_json_1_0(
                item
            )
        )
    return out
