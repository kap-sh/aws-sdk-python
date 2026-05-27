"""Generated from Smithy shape ``com.amazonaws.ec2#DescribePrincipalIdFormat``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_principal_id_format_request
    import aws_sdk_ec2.types.describe_principal_id_format_result


def describe_principal_id_format(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_principal_id_format_request.DescribePrincipalIdFormatRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_principal_id_format_result.DescribePrincipalIdFormatResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_principal_id_format(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_principal_id_format_request.DescribePrincipalIdFormatRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_principal_id_format_result.DescribePrincipalIdFormatResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
