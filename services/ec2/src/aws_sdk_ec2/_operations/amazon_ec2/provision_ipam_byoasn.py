"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionIpamByoasn``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.provision_ipam_byoasn_request
    import aws_sdk_ec2.types.provision_ipam_byoasn_result


def provision_ipam_byoasn(
    options: OperationOptions,
    input: aws_sdk_ec2.types.provision_ipam_byoasn_request.ProvisionIpamByoasnRequest,
) -> tuple[
    aws_sdk_ec2.types.provision_ipam_byoasn_result.ProvisionIpamByoasnResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_provision_ipam_byoasn(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.provision_ipam_byoasn_request.ProvisionIpamByoasnRequest,
) -> tuple[
    aws_sdk_ec2.types.provision_ipam_byoasn_result.ProvisionIpamByoasnResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
