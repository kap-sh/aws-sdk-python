"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateEnclaveCertificateIamRole``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disassociate_enclave_certificate_iam_role_request
    import aws_sdk_ec2.types.disassociate_enclave_certificate_iam_role_result


def disassociate_enclave_certificate_iam_role(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disassociate_enclave_certificate_iam_role_request.DisassociateEnclaveCertificateIamRoleRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_enclave_certificate_iam_role_result.DisassociateEnclaveCertificateIamRoleResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disassociate_enclave_certificate_iam_role(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disassociate_enclave_certificate_iam_role_request.DisassociateEnclaveCertificateIamRoleRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_enclave_certificate_iam_role_result.DisassociateEnclaveCertificateIamRoleResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
