"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInstanceEventWindow``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_instance_event_window_request
    import aws_sdk_ec2.types.create_instance_event_window_result


def create_instance_event_window(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_instance_event_window_request.CreateInstanceEventWindowRequest,
) -> tuple[
    aws_sdk_ec2.types.create_instance_event_window_result.CreateInstanceEventWindowResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_instance_event_window(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_instance_event_window_request.CreateInstanceEventWindowRequest,
) -> tuple[
    aws_sdk_ec2.types.create_instance_event_window_result.CreateInstanceEventWindowResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
