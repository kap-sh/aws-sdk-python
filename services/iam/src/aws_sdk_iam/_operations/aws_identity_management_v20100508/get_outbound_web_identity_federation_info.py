"""Generated from Smithy shape ``com.amazonaws.iam#GetOutboundWebIdentityFederationInfo``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_outbound_web_identity_federation_info_response


def get_outbound_web_identity_federation_info(
    options: OperationOptions,
) -> tuple[
    aws_sdk_iam.types.get_outbound_web_identity_federation_info_response.GetOutboundWebIdentityFederationInfoResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_outbound_web_identity_federation_info(
    options: AsyncOperationOptions,
) -> tuple[
    aws_sdk_iam.types.get_outbound_web_identity_federation_info_response.GetOutboundWebIdentityFederationInfoResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
