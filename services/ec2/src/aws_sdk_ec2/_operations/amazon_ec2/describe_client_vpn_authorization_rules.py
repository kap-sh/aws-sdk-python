"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClientVpnAuthorizationRules``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_client_vpn_authorization_rules_request
    import aws_sdk_ec2.types.describe_client_vpn_authorization_rules_result


def describe_client_vpn_authorization_rules(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_client_vpn_authorization_rules_request.DescribeClientVpnAuthorizationRulesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_client_vpn_authorization_rules_result.DescribeClientVpnAuthorizationRulesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_client_vpn_authorization_rules(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_client_vpn_authorization_rules_request.DescribeClientVpnAuthorizationRulesRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_client_vpn_authorization_rules_result.DescribeClientVpnAuthorizationRulesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
