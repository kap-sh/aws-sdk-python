"""Generated from Smithy shape ``com.amazonaws.kms#ImportKeyMaterial``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.import_key_material_request
    import awd_sdk_kms.types.import_key_material_response


def import_key_material(
    options: OperationOptions,
    input: awd_sdk_kms.types.import_key_material_request.ImportKeyMaterialRequest,
) -> tuple[
    awd_sdk_kms.types.import_key_material_response.ImportKeyMaterialResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_import_key_material(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.import_key_material_request.ImportKeyMaterialRequest,
) -> tuple[
    awd_sdk_kms.types.import_key_material_response.ImportKeyMaterialResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
