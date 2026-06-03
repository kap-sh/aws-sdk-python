"""Generated from Smithy shape ``com.amazonaws.kms#GetParametersForImport``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.get_parameters_for_import_request
    import awd_sdk_kms.types.get_parameters_for_import_response


def get_parameters_for_import(
    options: OperationOptions,
    input: awd_sdk_kms.types.get_parameters_for_import_request.GetParametersForImportRequest,
) -> tuple[
    awd_sdk_kms.types.get_parameters_for_import_response.GetParametersForImportResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_parameters_for_import(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.get_parameters_for_import_request.GetParametersForImportRequest,
) -> tuple[
    awd_sdk_kms.types.get_parameters_for_import_response.GetParametersForImportResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
