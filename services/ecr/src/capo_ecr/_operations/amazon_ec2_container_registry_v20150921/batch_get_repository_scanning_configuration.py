"""Generated from Smithy shape ``com.amazonaws.ecr#BatchGetRepositoryScanningConfiguration``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_ecr._auth._signers
import capo_ecr._auth._sigv4
import capo_ecr.errors.invalid_parameter_exception
import capo_ecr.errors.repository_not_found_exception
import capo_ecr.errors.server_exception
import capo_ecr.errors.validation_exception
import capo_ecr.types.batch_get_repository_scanning_configuration_request
import capo_ecr.types.batch_get_repository_scanning_configuration_response
import capo_ecr.types.repository_scanning_configuration_failure_list
import capo_ecr.types.repository_scanning_configuration_list
import capo_ecr.types.scanning_configuration_repository_name_list
from capo_ecr._protocol.errors import parse_error_metadata_json
from capo_ecr._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_ecr._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_ecr.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "InvalidParameterException":
            raise capo_ecr.errors.invalid_parameter_exception.InvalidParameterException.from_aws_json_1_1(
                data
            )
        case "RepositoryNotFoundException":
            raise capo_ecr.errors.repository_not_found_exception.RepositoryNotFoundException.from_aws_json_1_1(
                data
            )
        case "ServerException":
            raise capo_ecr.errors.server_exception.ServerException.from_aws_json_1_1(
                data
            )
        case "ValidationException":
            raise capo_ecr.errors.validation_exception.ValidationException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_ecr.types.batch_get_repository_scanning_configuration_response.BatchGetRepositoryScanningConfigurationResponse:
    out: capo_ecr.types.batch_get_repository_scanning_configuration_response.BatchGetRepositoryScanningConfigurationResponse = capo_ecr.types.batch_get_repository_scanning_configuration_response.deserialize_aws_json_1_1(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_ecr.types.batch_get_repository_scanning_configuration_response.BatchGetRepositoryScanningConfigurationResponse:
    out: capo_ecr.types.batch_get_repository_scanning_configuration_response.BatchGetRepositoryScanningConfigurationResponse = capo_ecr.types.batch_get_repository_scanning_configuration_response.deserialize_aws_json_1_1(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_ecr._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_ecr._auth._sigv4.build_sigv4_auth_scheme("ecr", options.region)
        )
        if sigv4_config is not None:
            return capo_ecr._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_ecr.types.batch_get_repository_scanning_configuration_request.BatchGetRepositoryScanningConfigurationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
            Region=options.region,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + ""
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    headers["X-Amz-Target"] = (
        "AmazonEC2ContainerRegistry_V20150921.BatchGetRepositoryScanningConfiguration"
    )
    body: bytes | None = json.dumps(
        capo_ecr.types.batch_get_repository_scanning_configuration_request.serialize_aws_json_1_1(
            input_
        )
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def batch_get_repository_scanning_configuration(
    options: OperationOptions,
    input_: capo_ecr.types.batch_get_repository_scanning_configuration_request.BatchGetRepositoryScanningConfigurationRequest,
) -> tuple[
    capo_ecr.types.batch_get_repository_scanning_configuration_response.BatchGetRepositoryScanningConfigurationResponse,
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


async def async_batch_get_repository_scanning_configuration(
    options: AsyncOperationOptions,
    input_: capo_ecr.types.batch_get_repository_scanning_configuration_request.BatchGetRepositoryScanningConfigurationRequest,
) -> tuple[
    capo_ecr.types.batch_get_repository_scanning_configuration_response.BatchGetRepositoryScanningConfigurationResponse,
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
