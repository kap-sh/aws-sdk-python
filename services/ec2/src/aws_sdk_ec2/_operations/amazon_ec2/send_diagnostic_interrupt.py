"""Generated from Smithy shape ``com.amazonaws.ec2#SendDiagnosticInterrupt``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.send_diagnostic_interrupt_request


def send_diagnostic_interrupt(
    options: OperationOptions,
    input: aws_sdk_ec2.types.send_diagnostic_interrupt_request.SendDiagnosticInterruptRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_send_diagnostic_interrupt(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.send_diagnostic_interrupt_request.SendDiagnosticInterruptRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
