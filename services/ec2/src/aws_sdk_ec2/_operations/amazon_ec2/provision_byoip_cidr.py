"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionByoipCidr``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.provision_byoip_cidr_request
    import aws_sdk_ec2.types.provision_byoip_cidr_result


def provision_byoip_cidr(
    options: OperationOptions,
    input: aws_sdk_ec2.types.provision_byoip_cidr_request.ProvisionByoipCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.provision_byoip_cidr_result.ProvisionByoipCidrResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_provision_byoip_cidr(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.provision_byoip_cidr_request.ProvisionByoipCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.provision_byoip_cidr_result.ProvisionByoipCidrResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
