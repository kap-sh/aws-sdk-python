"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIdFormat``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_id_format_request


def modify_id_format(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_id_format_request.ModifyIdFormatRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_id_format(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_id_format_request.ModifyIdFormatRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
