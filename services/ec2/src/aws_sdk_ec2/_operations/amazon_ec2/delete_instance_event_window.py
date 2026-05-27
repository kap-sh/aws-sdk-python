"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteInstanceEventWindow``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_instance_event_window_request
    import aws_sdk_ec2.types.delete_instance_event_window_result


def delete_instance_event_window(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_instance_event_window_request.DeleteInstanceEventWindowRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_instance_event_window_result.DeleteInstanceEventWindowResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_instance_event_window(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_instance_event_window_request.DeleteInstanceEventWindowRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_instance_event_window_result.DeleteInstanceEventWindowResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
