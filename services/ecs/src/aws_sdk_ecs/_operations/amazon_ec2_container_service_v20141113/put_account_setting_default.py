"""Generated from Smithy shape ``com.amazonaws.ecs#PutAccountSettingDefault``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.put_account_setting_default_request
    import aws_sdk_ecs.types.put_account_setting_default_response


def put_account_setting_default(
    options: OperationOptions,
    input: aws_sdk_ecs.types.put_account_setting_default_request.PutAccountSettingDefaultRequest,
) -> tuple[
    aws_sdk_ecs.types.put_account_setting_default_response.PutAccountSettingDefaultResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_put_account_setting_default(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.put_account_setting_default_request.PutAccountSettingDefaultRequest,
) -> tuple[
    aws_sdk_ecs.types.put_account_setting_default_response.PutAccountSettingDefaultResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
