"""Generated from Smithy shape ``com.amazonaws.iam#SetSecurityTokenServicePreferences``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.set_security_token_service_preferences_request


def set_security_token_service_preferences(
    options: OperationOptions,
    input: aws_sdk_iam.types.set_security_token_service_preferences_request.SetSecurityTokenServicePreferencesRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_set_security_token_service_preferences(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.set_security_token_service_preferences_request.SetSecurityTokenServicePreferencesRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
