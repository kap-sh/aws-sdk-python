"""Generated from Smithy shape ``com.amazonaws.kms#ScheduleKeyDeletion``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.schedule_key_deletion_request
    import awd_sdk_kms.types.schedule_key_deletion_response


def schedule_key_deletion(
    options: OperationOptions,
    input: awd_sdk_kms.types.schedule_key_deletion_request.ScheduleKeyDeletionRequest,
) -> tuple[
    awd_sdk_kms.types.schedule_key_deletion_response.ScheduleKeyDeletionResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_schedule_key_deletion(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.schedule_key_deletion_request.ScheduleKeyDeletionRequest,
) -> tuple[
    awd_sdk_kms.types.schedule_key_deletion_response.ScheduleKeyDeletionResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
