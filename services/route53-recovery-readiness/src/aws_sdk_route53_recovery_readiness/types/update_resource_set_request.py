"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#UpdateResourceSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__list_of_resource
    import aws_sdk_route53_recovery_readiness.types.__string
    import aws_sdk_route53_recovery_readiness.types.__string_pattern_awsa_za_z09_a_za_z09


class UpdateResourceSetRequest(TypedDict):
    resource_set_name: "aws_sdk_route53_recovery_readiness.types.__string.__string"
    """<p>Name of a resource set.</p>"""
    resource_set_type: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string_pattern_awsa_za_z09_a_za_z09.__stringPatternAWSAZaZ09AZaZ09"
    ]
    """<p>The resource type of the resources in the resource set. Enter one of the following values for resource type:</p> <p>AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource</p>"""
    resources: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__list_of_resource.__listOfResource"
    ]
    """<p>A list of resource objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResourceSetRequest) -> dict:
    out: dict = {}
    if "resource_set_type" in value:
        out["resourceSetType"] = value["resource_set_type"]
    if "resources" in value:
        import aws_sdk_route53_recovery_readiness.types.__list_of_resource

        out["resources"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_resource.serialize_json(
                value["resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateResourceSetRequest:
    out: UpdateResourceSetRequest = {}  # type: ignore[typeddict-item]
    if "resourceSetType" in data:
        out["resource_set_type"] = data["resourceSetType"]
    if "resources" in data:
        import aws_sdk_route53_recovery_readiness.types.__list_of_resource

        out["resources"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_resource.deserialize_json(
                data["resources"]
            )
        )
    return out
