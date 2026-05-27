"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateSecurityGroupRuleDescriptionsIngress``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.update_security_group_rule_descriptions_ingress_request
    import aws_sdk_ec2.types.update_security_group_rule_descriptions_ingress_result


def update_security_group_rule_descriptions_ingress(
    options: OperationOptions,
    input: aws_sdk_ec2.types.update_security_group_rule_descriptions_ingress_request.UpdateSecurityGroupRuleDescriptionsIngressRequest,
) -> tuple[
    aws_sdk_ec2.types.update_security_group_rule_descriptions_ingress_result.UpdateSecurityGroupRuleDescriptionsIngressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_security_group_rule_descriptions_ingress(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.update_security_group_rule_descriptions_ingress_request.UpdateSecurityGroupRuleDescriptionsIngressRequest,
) -> tuple[
    aws_sdk_ec2.types.update_security_group_rule_descriptions_ingress_result.UpdateSecurityGroupRuleDescriptionsIngressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
