"""Generated from Smithy shape ``com.amazonaws.ec2#ExportImage``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_image_request
    import aws_sdk_ec2.types.export_image_result


def export_image(
    options: OperationOptions,
    input: aws_sdk_ec2.types.export_image_request.ExportImageRequest,
) -> tuple[aws_sdk_ec2.types.export_image_result.ExportImageResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_export_image(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.export_image_request.ExportImageRequest,
) -> tuple[aws_sdk_ec2.types.export_image_result.ExportImageResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
