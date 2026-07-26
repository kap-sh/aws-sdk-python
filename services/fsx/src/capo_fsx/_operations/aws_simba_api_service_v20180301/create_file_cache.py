"""Generated from Smithy shape ``com.amazonaws.fsx#CreateFileCache``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_fsx._auth._signers
import capo_fsx._auth._sigv4
import capo_fsx.errors.bad_request
import capo_fsx.errors.incompatible_parameter_error
import capo_fsx.errors.internal_server_error
import capo_fsx.errors.invalid_network_settings
import capo_fsx.errors.invalid_per_unit_storage_throughput
import capo_fsx.errors.missing_file_cache_configuration
import capo_fsx.errors.service_limit_exceeded
import capo_fsx.types.create_file_cache_data_repository_associations
import capo_fsx.types.create_file_cache_lustre_configuration
import capo_fsx.types.create_file_cache_request
import capo_fsx.types.create_file_cache_response
import capo_fsx.types.file_cache_creating
import capo_fsx.types.file_cache_type
import capo_fsx.types.security_group_ids
import capo_fsx.types.subnet_ids
import capo_fsx.types.tags
from capo_fsx._protocol.errors import parse_error_metadata_json
from capo_fsx._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_fsx._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_fsx.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "BadRequest":
            raise capo_fsx.errors.bad_request.BadRequest.from_aws_json_1_1(data)
        case "IncompatibleParameterError":
            raise capo_fsx.errors.incompatible_parameter_error.IncompatibleParameterError.from_aws_json_1_1(
                data
            )
        case "InternalServerError":
            raise capo_fsx.errors.internal_server_error.InternalServerError.from_aws_json_1_1(
                data
            )
        case "InvalidNetworkSettings":
            raise capo_fsx.errors.invalid_network_settings.InvalidNetworkSettings.from_aws_json_1_1(
                data
            )
        case "InvalidPerUnitStorageThroughput":
            raise capo_fsx.errors.invalid_per_unit_storage_throughput.InvalidPerUnitStorageThroughput.from_aws_json_1_1(
                data
            )
        case "MissingFileCacheConfiguration":
            raise capo_fsx.errors.missing_file_cache_configuration.MissingFileCacheConfiguration.from_aws_json_1_1(
                data
            )
        case "ServiceLimitExceeded":
            raise capo_fsx.errors.service_limit_exceeded.ServiceLimitExceeded.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_fsx.types.create_file_cache_response.CreateFileCacheResponse:
    out: capo_fsx.types.create_file_cache_response.CreateFileCacheResponse = (
        capo_fsx.types.create_file_cache_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_fsx.types.create_file_cache_response.CreateFileCacheResponse:
    out: capo_fsx.types.create_file_cache_response.CreateFileCacheResponse = (
        capo_fsx.types.create_file_cache_response.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_fsx._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_fsx._auth._sigv4.build_sigv4_auth_scheme("fsx", options.region)
        )
        if sigv4_config is not None:
            return capo_fsx._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_fsx.types.create_file_cache_request.CreateFileCacheRequest,
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
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = "AWSSimbaAPIService_v20180301.CreateFileCache"
    body: bytes | None = json.dumps(
        capo_fsx.types.create_file_cache_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_file_cache(
    options: OperationOptions,
    input_: capo_fsx.types.create_file_cache_request.CreateFileCacheRequest,
) -> tuple[
    capo_fsx.types.create_file_cache_response.CreateFileCacheResponse, zapros.Response
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


async def async_create_file_cache(
    options: AsyncOperationOptions,
    input_: capo_fsx.types.create_file_cache_request.CreateFileCacheRequest,
) -> tuple[
    capo_fsx.types.create_file_cache_response.CreateFileCacheResponse, zapros.Response
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
