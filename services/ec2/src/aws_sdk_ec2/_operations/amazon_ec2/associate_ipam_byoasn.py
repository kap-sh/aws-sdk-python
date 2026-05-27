"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateIpamByoasn``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associate_ipam_byoasn_request
    import aws_sdk_ec2.types.associate_ipam_byoasn_result


def associate_ipam_byoasn(
    options: OperationOptions,
    input: aws_sdk_ec2.types.associate_ipam_byoasn_request.AssociateIpamByoasnRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_ipam_byoasn_result.AssociateIpamByoasnResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_associate_ipam_byoasn(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.associate_ipam_byoasn_request.AssociateIpamByoasnRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_ipam_byoasn_result.AssociateIpamByoasnResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
