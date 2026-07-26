"""Generated from Smithy shape ``com.amazonaws.backup#RevokeRestoreAccessBackupVault``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_backup._auth._signers
import capo_backup._auth._sigv4
import capo_backup.errors.invalid_parameter_value_exception
import capo_backup.errors.invalid_request_exception
import capo_backup.errors.missing_parameter_value_exception
import capo_backup.errors.resource_not_found_exception
import capo_backup.errors.service_unavailable_exception
import capo_backup.types.revoke_restore_access_backup_vault_input
from capo_backup._protocol.errors import parse_error_metadata_json
from capo_backup._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_backup._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_backup.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterValueException":
            raise capo_backup.errors.invalid_parameter_value_exception.InvalidParameterValueException.from_json(
                data
            )
        case "InvalidRequestException":
            raise capo_backup.errors.invalid_request_exception.InvalidRequestException.from_json(
                data
            )
        case "MissingParameterValueException":
            raise capo_backup.errors.missing_parameter_value_exception.MissingParameterValueException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise capo_backup.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ServiceUnavailableException":
            raise capo_backup.errors.service_unavailable_exception.ServiceUnavailableException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_backup._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_backup._auth._sigv4.build_sigv4_auth_scheme(
                "backup", options.region
            )
        )
        if sigv4_config is not None:
            return capo_backup._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_backup.types.revoke_restore_access_backup_vault_input.RevokeRestoreAccessBackupVaultInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/")
        + "/logically-air-gapped-backup-vaults/{BackupVaultName}/restore-access-backup-vaults/{RestoreAccessBackupVaultArn}"
    )
    url = url.replace(
        "{BackupVaultName}", quote(str(input_["backup_vault_name"]), safe="")
    )
    url = url.replace(
        "{RestoreAccessBackupVaultArn}",
        quote(str(input_["restore_access_backup_vault_arn"]), safe=""),
    )
    params: dict[str, str] = {}
    if "requester_comment" in input_:
        params["requesterComment"] = str(input_["requester_comment"])
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "DELETE", headers=headers, body=body, context={"signer": signer}
    )


def revoke_restore_access_backup_vault(
    options: OperationOptions,
    input_: capo_backup.types.revoke_restore_access_backup_vault_input.RevokeRestoreAccessBackupVaultInput,
) -> tuple[None, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return None, response
    except BaseException:
        response.close()
        raise


async def async_revoke_restore_access_backup_vault(
    options: AsyncOperationOptions,
    input_: capo_backup.types.revoke_restore_access_backup_vault_input.RevokeRestoreAccessBackupVaultInput,
) -> tuple[None, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return None, response
    except BaseException:
        await response.aclose()
        raise
