"""Generated from Smithy shape ``com.amazonaws.ec2#RevokeSecurityGroupIngress``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.revoke_security_group_ingress_request
    import aws_sdk_ec2.types.revoke_security_group_ingress_result


def revoke_security_group_ingress(
    options: OperationOptions,
    input: aws_sdk_ec2.types.revoke_security_group_ingress_request.RevokeSecurityGroupIngressRequest,
) -> tuple[
    aws_sdk_ec2.types.revoke_security_group_ingress_result.RevokeSecurityGroupIngressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_revoke_security_group_ingress(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.revoke_security_group_ingress_request.RevokeSecurityGroupIngressRequest,
) -> tuple[
    aws_sdk_ec2.types.revoke_security_group_ingress_result.RevokeSecurityGroupIngressResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
