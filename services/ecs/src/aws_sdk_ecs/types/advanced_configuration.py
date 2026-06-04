"""Generated from Smithy shape ``com.amazonaws.ecs#AdvancedConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class AdvancedConfiguration(TypedDict):
    alternate_target_group_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the alternate target group for Amazon ECS blue/green deployments.</p>"""
    production_listener_rule: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that that identifies the production listener rule (in the case of an Application Load Balancer) or listener (in the case for an Network Load Balancer) for routing production traffic.</p>"""
    test_listener_rule: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that identifies ) that identifies the test listener rule (in the case of an Application Load Balancer) or listener (in the case for an Network Load Balancer) for routing test traffic.</p>"""
    role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants Amazon ECS permission to call the Elastic Load Balancing APIs for you.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdvancedConfiguration) -> dict:
    out: dict = {}
    if "alternate_target_group_arn" in value:
        out["alternateTargetGroupArn"] = value["alternate_target_group_arn"]
    if "production_listener_rule" in value:
        out["productionListenerRule"] = value["production_listener_rule"]
    if "test_listener_rule" in value:
        out["testListenerRule"] = value["test_listener_rule"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdvancedConfiguration:
    out: AdvancedConfiguration = {}  # type: ignore[typeddict-item]
    if "alternateTargetGroupArn" in data:
        out["alternate_target_group_arn"] = data["alternateTargetGroupArn"]
    if "productionListenerRule" in data:
        out["production_listener_rule"] = data["productionListenerRule"]
    if "testListenerRule" in data:
        out["test_listener_rule"] = data["testListenerRule"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    return out
