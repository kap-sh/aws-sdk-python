"""Generated from Smithy shape ``com.amazonaws.efs#UpdateFileSystemProtection``."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import quote

import zapros
from typing_extensions import Never

import aws_sdk_efs._auth._signers
import aws_sdk_efs._auth._sigv4
import aws_sdk_efs.errors.bad_request
import aws_sdk_efs.errors.file_system_not_found
import aws_sdk_efs.errors.incorrect_file_system_life_cycle_state
import aws_sdk_efs.errors.insufficient_throughput_capacity
import aws_sdk_efs.errors.internal_server_error
import aws_sdk_efs.errors.replication_already_exists
import aws_sdk_efs.errors.throughput_limit_exceeded
import aws_sdk_efs.errors.too_many_requests
import aws_sdk_efs.types.file_system_protection_description
import aws_sdk_efs.types.replication_overwrite_protection
import aws_sdk_efs.types.update_file_system_protection_request
from aws_sdk_efs._protocol.errors import parse_error_metadata_json
from aws_sdk_efs._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_efs._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_efs.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequest":
            raise aws_sdk_efs.errors.bad_request.BadRequest.from_json(data)
        case "FileSystemNotFound":
            raise aws_sdk_efs.errors.file_system_not_found.FileSystemNotFound.from_json(
                data
            )
        case "IncorrectFileSystemLifeCycleState":
            raise aws_sdk_efs.errors.incorrect_file_system_life_cycle_state.IncorrectFileSystemLifeCycleState.from_json(
                data
            )
        case "InsufficientThroughputCapacity":
            raise aws_sdk_efs.errors.insufficient_throughput_capacity.InsufficientThroughputCapacity.from_json(
                data
            )
        case "InternalServerError":
            raise aws_sdk_efs.errors.internal_server_error.InternalServerError.from_json(
                data
            )
        case "ReplicationAlreadyExists":
            raise aws_sdk_efs.errors.replication_already_exists.ReplicationAlreadyExists.from_json(
                data
            )
        case "ThroughputLimitExceeded":
            raise aws_sdk_efs.errors.throughput_limit_exceeded.ThroughputLimitExceeded.from_json(
                data
            )
        case "TooManyRequests":
            raise aws_sdk_efs.errors.too_many_requests.TooManyRequests.from_json(data)
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_efs.types.file_system_protection_description.FileSystemProtectionDescription
):
    out: aws_sdk_efs.types.file_system_protection_description.FileSystemProtectionDescription = aws_sdk_efs.types.file_system_protection_description.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> (
    aws_sdk_efs.types.file_system_protection_description.FileSystemProtectionDescription
):
    out: aws_sdk_efs.types.file_system_protection_description.FileSystemProtectionDescription = aws_sdk_efs.types.file_system_protection_description.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_efs._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_efs._auth._sigv4.build_sigv4_auth_scheme(
                "elasticfilesystem", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_efs._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_efs.types.update_file_system_protection_request.UpdateFileSystemProtectionRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = (
        endpoint.url.rstrip("/") + "/2015-02-01/file-systems/{FileSystemId}/protection"
    )
    url = url.replace("{FileSystemId}", quote(str(input_["file_system_id"]), safe=""))
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        aws_sdk_efs.types.update_file_system_protection_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "PUT", headers=headers, body=body, context={"signer": signer}
    )


def update_file_system_protection(
    options: OperationOptions,
    input_: aws_sdk_efs.types.update_file_system_protection_request.UpdateFileSystemProtectionRequest,
) -> tuple[
    aws_sdk_efs.types.file_system_protection_description.FileSystemProtectionDescription,
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


async def async_update_file_system_protection(
    options: AsyncOperationOptions,
    input_: aws_sdk_efs.types.update_file_system_protection_request.UpdateFileSystemProtectionRequest,
) -> tuple[
    aws_sdk_efs.types.file_system_protection_description.FileSystemProtectionDescription,
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
