"""Generated from Smithy shape ``com.amazonaws.ec2#AuthorizeSecurityGroupEgress``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.authorize_security_group_egress_request
    import aws_sdk_ec2.types.authorize_security_group_egress_result


def authorize_security_group_egress(
    options: OperationOptions,
    input: aws_sdk_ec2.types.authorize_security_group_egress_request.AuthorizeSecurityGroupEgressRequest,
) -> tuple[
    aws_sdk_ec2.types.authorize_security_group_egress_result.AuthorizeSecurityGroupEgressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_authorize_security_group_egress(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.authorize_security_group_egress_request.AuthorizeSecurityGroupEgressRequest,
) -> tuple[
    aws_sdk_ec2.types.authorize_security_group_egress_result.AuthorizeSecurityGroupEgressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
