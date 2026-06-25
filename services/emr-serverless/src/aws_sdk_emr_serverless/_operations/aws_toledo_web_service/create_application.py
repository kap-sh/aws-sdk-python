"""Generated from Smithy shape ``com.amazonaws.emrserverless#CreateApplication``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_emr_serverless._auth._signers
import aws_sdk_emr_serverless._auth._sigv4
import aws_sdk_emr_serverless.errors.conflict_exception
import aws_sdk_emr_serverless.errors.internal_server_exception
import aws_sdk_emr_serverless.errors.resource_not_found_exception
import aws_sdk_emr_serverless.errors.validation_exception
import aws_sdk_emr_serverless.types.auto_start_config
import aws_sdk_emr_serverless.types.auto_stop_config
import aws_sdk_emr_serverless.types.configuration_list
import aws_sdk_emr_serverless.types.create_application_request
import aws_sdk_emr_serverless.types.create_application_response
import aws_sdk_emr_serverless.types.disk_encryption_configuration
import aws_sdk_emr_serverless.types.identity_center_configuration_input
import aws_sdk_emr_serverless.types.image_configuration_input
import aws_sdk_emr_serverless.types.initial_capacity_config_map
import aws_sdk_emr_serverless.types.interactive_configuration
import aws_sdk_emr_serverless.types.job_level_cost_allocation_configuration
import aws_sdk_emr_serverless.types.maximum_allowed_resources
import aws_sdk_emr_serverless.types.monitoring_configuration
import aws_sdk_emr_serverless.types.network_configuration
import aws_sdk_emr_serverless.types.scheduler_configuration
import aws_sdk_emr_serverless.types.tag_map
import aws_sdk_emr_serverless.types.worker_type_specification_input_map
from aws_sdk_emr_serverless._protocol.errors import parse_error_metadata_json
from aws_sdk_emr_serverless._rule_engine._endpoint_rule_set import (
    EndpointParams,
    resolve,
)
from aws_sdk_emr_serverless._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)
from aws_sdk_emr_serverless.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "ConflictException":
            raise aws_sdk_emr_serverless.errors.conflict_exception.ConflictException.from_json(
                data
            )
        case "InternalServerException":
            raise aws_sdk_emr_serverless.errors.internal_server_exception.InternalServerException.from_json(
                data
            )
        case "ResourceNotFoundException":
            raise aws_sdk_emr_serverless.errors.resource_not_found_exception.ResourceNotFoundException.from_json(
                data
            )
        case "ValidationException":
            raise aws_sdk_emr_serverless.errors.validation_exception.ValidationException.from_json(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_emr_serverless.types.create_application_response.CreateApplicationResponse:
    out: aws_sdk_emr_serverless.types.create_application_response.CreateApplicationResponse = aws_sdk_emr_serverless.types.create_application_response.deserialize_json(
        json.loads(response.read())
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_emr_serverless.types.create_application_response.CreateApplicationResponse:
    out: aws_sdk_emr_serverless.types.create_application_response.CreateApplicationResponse = aws_sdk_emr_serverless.types.create_application_response.deserialize_json(
        json.loads(await response.aread())
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_emr_serverless._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_emr_serverless._auth._sigv4.build_sigv4_auth_scheme(
                "emr-serverless", options.region
            )
        )
        if sigv4_config is not None:
            return aws_sdk_emr_serverless._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_emr_serverless.types.create_application_request.CreateApplicationRequest,
) -> zapros.Request:
    endpoint = resolve(
        EndpointParams(
            Region=options.region,
            UseDualStack=options.use_dual_stack,
            UseFIPS=options.use_fips,
            Endpoint=options.endpoint,
        )
    )  # noqa: F841
    url = endpoint.url.rstrip("/") + "/applications"
    params: dict[str, str] = {}
    headers: dict[str, str] = {k: ", ".join(v) for k, v in endpoint.headers.items()}
    body: bytes | None = json.dumps(
        aws_sdk_emr_serverless.types.create_application_request.serialize_json(input_)
    ).encode()
    headers["content-type"] = "application/json"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_application(
    options: OperationOptions,
    input_: aws_sdk_emr_serverless.types.create_application_request.CreateApplicationRequest,
) -> tuple[
    aws_sdk_emr_serverless.types.create_application_response.CreateApplicationResponse,
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


async def async_create_application(
    options: AsyncOperationOptions,
    input_: aws_sdk_emr_serverless.types.create_application_request.CreateApplicationRequest,
) -> tuple[
    aws_sdk_emr_serverless.types.create_application_response.CreateApplicationResponse,
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
