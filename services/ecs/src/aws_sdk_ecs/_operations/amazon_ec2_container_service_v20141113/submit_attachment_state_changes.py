"""Generated from Smithy shape ``com.amazonaws.ecs#SubmitAttachmentStateChanges``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ecs._auth._signers
from aws_sdk_ecs._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ecs.types.submit_attachment_state_changes_request
    import aws_sdk_ecs.types.submit_attachment_state_changes_response


def submit_attachment_state_changes(
    options: OperationOptions,
    input: aws_sdk_ecs.types.submit_attachment_state_changes_request.SubmitAttachmentStateChangesRequest,
) -> tuple[
    aws_sdk_ecs.types.submit_attachment_state_changes_response.SubmitAttachmentStateChangesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_submit_attachment_state_changes(
    options: AsyncOperationOptions,
    input: aws_sdk_ecs.types.submit_attachment_state_changes_request.SubmitAttachmentStateChangesRequest,
) -> tuple[
    aws_sdk_ecs.types.submit_attachment_state_changes_response.SubmitAttachmentStateChangesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
