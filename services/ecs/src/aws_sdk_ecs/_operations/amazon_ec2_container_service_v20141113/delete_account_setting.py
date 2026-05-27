"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteAccountSetting``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.delete_account_setting_request
    import aws_sdk_ecs.types.delete_account_setting_response


def delete_account_setting(
    options: OperationOptions,
    input: aws_sdk_ecs.types.delete_account_setting_request.DeleteAccountSettingRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_account_setting_response.DeleteAccountSettingResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_account_setting(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.delete_account_setting_request.DeleteAccountSettingRequest,
) -> tuple[
    aws_sdk_ecs.types.delete_account_setting_response.DeleteAccountSettingResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
