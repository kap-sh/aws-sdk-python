"""Generated from Smithy shape ``com.amazonaws.ec2#GetDefaultCreditSpecification``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_default_credit_specification_request
    import aws_sdk_ec2.types.get_default_credit_specification_result


def get_default_credit_specification(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_default_credit_specification_request.GetDefaultCreditSpecificationRequest,
) -> tuple[
    aws_sdk_ec2.types.get_default_credit_specification_result.GetDefaultCreditSpecificationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_default_credit_specification(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_default_credit_specification_request.GetDefaultCreditSpecificationRequest,
) -> tuple[
    aws_sdk_ec2.types.get_default_credit_specification_result.GetDefaultCreditSpecificationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
