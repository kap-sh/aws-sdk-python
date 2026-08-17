"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedInstancesNetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string_list


class ManagedInstancesNetworkConfiguration(TypedDict, closed=True):
    subnets: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The list of subnet IDs where Amazon ECS can launch Amazon ECS Managed Instances. Instances are distributed across the specified subnets for high availability. All subnets must be in the same VPC.</p>"""
    security_groups: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The list of security group IDs to apply to Amazon ECS Managed Instances. These security groups control the network traffic allowed to and from the instances.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedInstancesNetworkConfiguration) -> dict:
    out: dict = {}
    if "subnets" in value:
        import capo_ecs.types.string_list

        out["subnets"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["subnets"]
        )
    if "security_groups" in value:
        import capo_ecs.types.string_list

        out["securityGroups"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["security_groups"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedInstancesNetworkConfiguration:
    out: ManagedInstancesNetworkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("subnets") is not None:
        import capo_ecs.types.string_list

        out["subnets"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["subnets"]
        )
    if data.get("securityGroups") is not None:
        import capo_ecs.types.string_list

        out["security_groups"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["securityGroups"]
        )
    return out
