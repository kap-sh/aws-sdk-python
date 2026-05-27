"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateInstanceEventWindow``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disassociate_instance_event_window_request
    import aws_sdk_ec2.types.disassociate_instance_event_window_result


def disassociate_instance_event_window(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disassociate_instance_event_window_request.DisassociateInstanceEventWindowRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_instance_event_window_result.DisassociateInstanceEventWindowResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disassociate_instance_event_window(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disassociate_instance_event_window_request.DisassociateInstanceEventWindowRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_instance_event_window_result.DisassociateInstanceEventWindowResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
