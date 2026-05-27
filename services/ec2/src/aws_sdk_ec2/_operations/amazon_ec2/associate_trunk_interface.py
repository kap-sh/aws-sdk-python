"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateTrunkInterface``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associate_trunk_interface_request
    import aws_sdk_ec2.types.associate_trunk_interface_result


def associate_trunk_interface(
    options: OperationOptions,
    input: aws_sdk_ec2.types.associate_trunk_interface_request.AssociateTrunkInterfaceRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_trunk_interface_result.AssociateTrunkInterfaceResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_associate_trunk_interface(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.associate_trunk_interface_request.AssociateTrunkInterfaceRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_trunk_interface_result.AssociateTrunkInterfaceResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
