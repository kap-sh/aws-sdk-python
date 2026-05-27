"""Generated from Smithy shape ``com.amazonaws.s3#SelectObjectContent``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
from aws_sdk_s3._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_s3.types.select_object_content_request
    import aws_sdk_s3.types.select_object_content_output


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input: aws_sdk_s3.types.select_object_content_request.SelectObjectContentRequest,
) -> zapros.Request:
    raise NotImplementedError("event stream output is not yet supported")


def select_object_content(
    options: OperationOptions,
    input: aws_sdk_s3.types.select_object_content_request.SelectObjectContentRequest,
) -> tuple[
    aws_sdk_s3.types.select_object_content_output.SelectObjectContentOutput,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")


async def async_select_object_content(
    options: AsyncOperationOptions,
    input: aws_sdk_s3.types.select_object_content_request.SelectObjectContentRequest,
) -> tuple[
    aws_sdk_s3.types.select_object_content_output.SelectObjectContentOutput,
    zapros.Response,
]:
    raise NotImplementedError("event stream output is not yet supported")
