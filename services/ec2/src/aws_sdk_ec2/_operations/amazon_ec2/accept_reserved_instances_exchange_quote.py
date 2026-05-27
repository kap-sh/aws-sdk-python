"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptReservedInstancesExchangeQuote``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.accept_reserved_instances_exchange_quote_request
    import aws_sdk_ec2.types.accept_reserved_instances_exchange_quote_result


def accept_reserved_instances_exchange_quote(
    options: OperationOptions,
    input: aws_sdk_ec2.types.accept_reserved_instances_exchange_quote_request.AcceptReservedInstancesExchangeQuoteRequest,
) -> tuple[
    aws_sdk_ec2.types.accept_reserved_instances_exchange_quote_result.AcceptReservedInstancesExchangeQuoteResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_accept_reserved_instances_exchange_quote(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.accept_reserved_instances_exchange_quote_request.AcceptReservedInstancesExchangeQuoteRequest,
) -> tuple[
    aws_sdk_ec2.types.accept_reserved_instances_exchange_quote_result.AcceptReservedInstancesExchangeQuoteResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
