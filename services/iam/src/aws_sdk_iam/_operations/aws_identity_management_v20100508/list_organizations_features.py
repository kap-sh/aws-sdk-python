"""Generated from Smithy shape ``com.amazonaws.iam#ListOrganizationsFeatures``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_organizations_features_request
    import aws_sdk_iam.types.list_organizations_features_response


def list_organizations_features(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_organizations_features_request.ListOrganizationsFeaturesRequest,
) -> tuple[
    aws_sdk_iam.types.list_organizations_features_response.ListOrganizationsFeaturesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_organizations_features(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_organizations_features_request.ListOrganizationsFeaturesRequest,
) -> tuple[
    aws_sdk_iam.types.list_organizations_features_response.ListOrganizationsFeaturesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
