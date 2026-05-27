"""Generated from Smithy shape ``com.amazonaws.ec2#ImportClientVpnClientCertificateRevocationList``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_client_vpn_client_certificate_revocation_list_request
    import aws_sdk_ec2.types.import_client_vpn_client_certificate_revocation_list_result


def import_client_vpn_client_certificate_revocation_list(
    options: OperationOptions,
    input: aws_sdk_ec2.types.import_client_vpn_client_certificate_revocation_list_request.ImportClientVpnClientCertificateRevocationListRequest,
) -> tuple[
    aws_sdk_ec2.types.import_client_vpn_client_certificate_revocation_list_result.ImportClientVpnClientCertificateRevocationListResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_import_client_vpn_client_certificate_revocation_list(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.import_client_vpn_client_certificate_revocation_list_request.ImportClientVpnClientCertificateRevocationListRequest,
) -> tuple[
    aws_sdk_ec2.types.import_client_vpn_client_certificate_revocation_list_result.ImportClientVpnClientCertificateRevocationListResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
