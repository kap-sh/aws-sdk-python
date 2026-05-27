"""Generated from Smithy shape ``com.amazonaws.ec2#DisableVpcClassicLink``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_vpc_classic_link_request
    import aws_sdk_ec2.types.disable_vpc_classic_link_result


def disable_vpc_classic_link(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disable_vpc_classic_link_request.DisableVpcClassicLinkRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_vpc_classic_link_result.DisableVpcClassicLinkResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disable_vpc_classic_link(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disable_vpc_classic_link_request.DisableVpcClassicLinkRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_vpc_classic_link_result.DisableVpcClassicLinkResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
