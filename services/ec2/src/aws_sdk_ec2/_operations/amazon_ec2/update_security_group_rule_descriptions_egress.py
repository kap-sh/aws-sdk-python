"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateSecurityGroupRuleDescriptionsEgress``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.update_security_group_rule_descriptions_egress_request
    import aws_sdk_ec2.types.update_security_group_rule_descriptions_egress_result


def update_security_group_rule_descriptions_egress(
    options: OperationOptions,
    input: aws_sdk_ec2.types.update_security_group_rule_descriptions_egress_request.UpdateSecurityGroupRuleDescriptionsEgressRequest,
) -> tuple[
    aws_sdk_ec2.types.update_security_group_rule_descriptions_egress_result.UpdateSecurityGroupRuleDescriptionsEgressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_security_group_rule_descriptions_egress(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.update_security_group_rule_descriptions_egress_request.UpdateSecurityGroupRuleDescriptionsEgressRequest,
) -> tuple[
    aws_sdk_ec2.types.update_security_group_rule_descriptions_egress_result.UpdateSecurityGroupRuleDescriptionsEgressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
