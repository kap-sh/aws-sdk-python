"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ResourceSetOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__list_of_resource
    import aws_sdk_route53_recovery_readiness.types.__string_max64_pattern_aazaz09_z
    import aws_sdk_route53_recovery_readiness.types.__string_max256
    import aws_sdk_route53_recovery_readiness.types.__string_pattern_awsa_za_z09_a_za_z09
    import aws_sdk_route53_recovery_readiness.types.tags


class ResourceSetOutput(TypedDict):
    resource_set_arn: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string_max256.__stringMax256"
    ]
    """<p>The Amazon Resource Name (ARN) for the resource set.</p>"""
    resource_set_name: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string_max64_pattern_aazaz09_z.__stringMax64PatternAAZAZ09Z"
    ]
    """<p>The name of the resource set.</p>"""
    resource_set_type: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string_pattern_awsa_za_z09_a_za_z09.__stringPatternAWSAZaZ09AZaZ09"
    ]
    """<p>The resource type of the resources in the resource set. Enter one of the following values for resource type:</p> <p>AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource</p>"""
    resources: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__list_of_resource.__listOfResource"
    ]
    """<p>A list of resource objects.</p>"""
    tags: NotRequired["aws_sdk_route53_recovery_readiness.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSetOutput) -> dict:
    out: dict = {}
    if "resource_set_arn" in value:
        out["resourceSetArn"] = value["resource_set_arn"]
    if "resource_set_name" in value:
        out["resourceSetName"] = value["resource_set_name"]
    if "resource_set_type" in value:
        out["resourceSetType"] = value["resource_set_type"]
    if "resources" in value:
        import aws_sdk_route53_recovery_readiness.types.__list_of_resource

        out["resources"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_resource.serialize_json(
                value["resources"]
            )
        )
    if "tags" in value:
        import aws_sdk_route53_recovery_readiness.types.tags

        out["tags"] = aws_sdk_route53_recovery_readiness.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ResourceSetOutput:
    out: ResourceSetOutput = {}  # type: ignore[typeddict-item]
    if "resourceSetArn" in data:
        out["resource_set_arn"] = data["resourceSetArn"]
    if "resourceSetName" in data:
        out["resource_set_name"] = data["resourceSetName"]
    if "resourceSetType" in data:
        out["resource_set_type"] = data["resourceSetType"]
    if "resources" in data:
        import aws_sdk_route53_recovery_readiness.types.__list_of_resource

        out["resources"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_resource.deserialize_json(
                data["resources"]
            )
        )
    if "tags" in data:
        import aws_sdk_route53_recovery_readiness.types.tags

        out["tags"] = aws_sdk_route53_recovery_readiness.types.tags.deserialize_json(
            data["tags"]
        )
    return out
