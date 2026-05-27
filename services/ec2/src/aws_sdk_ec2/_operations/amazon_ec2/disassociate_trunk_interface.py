"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateTrunkInterface``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disassociate_trunk_interface_request
    import aws_sdk_ec2.types.disassociate_trunk_interface_result


def disassociate_trunk_interface(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disassociate_trunk_interface_request.DisassociateTrunkInterfaceRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_trunk_interface_result.DisassociateTrunkInterfaceResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disassociate_trunk_interface(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disassociate_trunk_interface_request.DisassociateTrunkInterfaceRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_trunk_interface_result.DisassociateTrunkInterfaceResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
