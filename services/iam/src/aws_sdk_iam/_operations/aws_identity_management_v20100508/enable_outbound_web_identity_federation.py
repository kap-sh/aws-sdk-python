"""Generated from Smithy shape ``com.amazonaws.iam#EnableOutboundWebIdentityFederation``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.enable_outbound_web_identity_federation_response


def enable_outbound_web_identity_federation(
    options: OperationOptions,
) -> tuple[
    aws_sdk_iam.types.enable_outbound_web_identity_federation_response.EnableOutboundWebIdentityFederationResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_outbound_web_identity_federation(
    options: AsyncOperationOptions,
) -> tuple[
    aws_sdk_iam.types.enable_outbound_web_identity_federation_response.EnableOutboundWebIdentityFederationResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
