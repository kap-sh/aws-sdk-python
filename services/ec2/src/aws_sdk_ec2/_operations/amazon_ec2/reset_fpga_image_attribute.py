"""Generated from Smithy shape ``com.amazonaws.ec2#ResetFpgaImageAttribute``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reset_fpga_image_attribute_request
    import aws_sdk_ec2.types.reset_fpga_image_attribute_result


def reset_fpga_image_attribute(
    options: OperationOptions,
    input: aws_sdk_ec2.types.reset_fpga_image_attribute_request.ResetFpgaImageAttributeRequest,
) -> tuple[
    aws_sdk_ec2.types.reset_fpga_image_attribute_result.ResetFpgaImageAttributeResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_reset_fpga_image_attribute(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.reset_fpga_image_attribute_request.ResetFpgaImageAttributeRequest,
) -> tuple[
    aws_sdk_ec2.types.reset_fpga_image_attribute_result.ResetFpgaImageAttributeResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
