"""Generated from Smithy shape ``com.amazonaws.odb#DeleteAutonomousDatabaseBackup``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import capo_odb._auth._signers
import capo_odb._auth._sigv4
import capo_odb.errors.access_denied_exception
import capo_odb.errors.conflict_exception
import capo_odb.errors.internal_server_exception
import capo_odb.errors.resource_not_found_exception
import capo_odb.errors.throttling_exception
import capo_odb.errors.validation_exception
import capo_odb.types.delete_autonomous_database_backup_input
import capo_odb.types.delete_autonomous_database_backup_output
from capo_odb._protocol.errors import parse_error_metadata_json
from capo_odb._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_odb._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_odb.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AccessDeniedException":
            raise capo_odb.errors.access_denied_exception.AccessDeniedException.from_aws_json_1_0(
                data
            )
        case "ConflictException":
            raise capo_odb.errors.conflict_exception.ConflictException.from_aws_json_1_0(
                data
            )
        case "InternalServerException":
            raise capo_odb.errors.internal_server_exception.InternalServerException.from_aws_json_1_0(
                data
            )
        case "ResourceNotFoundException":
            raise capo_odb.errors.resource_not_found_exception.ResourceNotFoundException.from_aws_json_1_0(
                data
            )
        case "ThrottlingException":
            raise capo_odb.errors.throttling_exception.ThrottlingException.from_aws_json_1_0(
                data
            )
        case "ValidationException":
            raise capo_odb.errors.validation_exception.ValidationException.from_aws_json_1_0(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_odb.types.delete_autonomous_database_backup_output.DeleteAutonomousDatabaseBackupOutput:
    out: capo_odb.types.delete_autonomous_database_backup_output.DeleteAutonomousDatabaseBackupOutput = {}  # type: ignore[typeddict-item]
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_odb.types.delete_autonomous_database_backup_output.DeleteAutonomousDatabaseBackupOutput:
    out: capo_odb.types.delete_autonomous_database_backup_output.DeleteAutonomousDatabaseBackupOutput = {}  # type: ignore[typeddict-item]
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_odb._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_odb._auth._sigv4.build_sigv4_auth_scheme("odb", options.region)
        )
        if sigv4_config is not None:
            return capo_odb._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_odb.types.delete_autonomous_database_backup_input.DeleteAutonomousDatabaseBackupInput,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    url = url.replace(
        "{autonomousDatabaseBackupId}",
        quote(str(input_["autonomous_database_backup_id"]), safe=""),
    )
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "Odb.DeleteAutonomousDatabaseBackup"
    body: bytes | None = b""
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def delete_autonomous_database_backup(
    options: OperationOptions,
    input_: capo_odb.types.delete_autonomous_database_backup_input.DeleteAutonomousDatabaseBackupInput,
) -> tuple[
    capo_odb.types.delete_autonomous_database_backup_output.DeleteAutonomousDatabaseBackupOutput,
    zapros.Response,
]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_delete_autonomous_database_backup(
    options: AsyncOperationOptions,
    input_: capo_odb.types.delete_autonomous_database_backup_input.DeleteAutonomousDatabaseBackupInput,
) -> tuple[
    capo_odb.types.delete_autonomous_database_backup_output.DeleteAutonomousDatabaseBackupOutput,
    zapros.Response,
]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
