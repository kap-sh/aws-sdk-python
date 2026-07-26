"""Generated from Smithy shape ``com.amazonaws.glue#CreateJob``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import capo_glue._auth._signers
import capo_glue._auth._sigv4
import capo_glue.errors.already_exists_exception
import capo_glue.errors.concurrent_modification_exception
import capo_glue.errors.idempotent_parameter_mismatch_exception
import capo_glue.errors.internal_service_exception
import capo_glue.errors.invalid_input_exception
import capo_glue.errors.operation_timeout_exception
import capo_glue.errors.resource_number_limit_exceeded_exception
import capo_glue.types.code_gen_configuration_nodes
import capo_glue.types.connections_list
import capo_glue.types.create_job_request
import capo_glue.types.create_job_response
import capo_glue.types.execution_class
import capo_glue.types.execution_property
import capo_glue.types.generic_map
import capo_glue.types.job_command
import capo_glue.types.job_mode
import capo_glue.types.notification_property
import capo_glue.types.source_control_details
import capo_glue.types.tags_map
import capo_glue.types.worker_type
from capo_glue._protocol.errors import parse_error_metadata_json
from capo_glue._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_glue._services._pipeline import AsyncOperationOptions, OperationOptions
from capo_glue.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AlreadyExistsException":
            raise capo_glue.errors.already_exists_exception.AlreadyExistsException.from_aws_json_1_1(
                data
            )
        case "ConcurrentModificationException":
            raise capo_glue.errors.concurrent_modification_exception.ConcurrentModificationException.from_aws_json_1_1(
                data
            )
        case "IdempotentParameterMismatchException":
            raise capo_glue.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException.from_aws_json_1_1(
                data
            )
        case "InternalServiceException":
            raise capo_glue.errors.internal_service_exception.InternalServiceException.from_aws_json_1_1(
                data
            )
        case "InvalidInputException":
            raise capo_glue.errors.invalid_input_exception.InvalidInputException.from_aws_json_1_1(
                data
            )
        case "OperationTimeoutException":
            raise capo_glue.errors.operation_timeout_exception.OperationTimeoutException.from_aws_json_1_1(
                data
            )
        case "ResourceNumberLimitExceededException":
            raise capo_glue.errors.resource_number_limit_exceeded_exception.ResourceNumberLimitExceededException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> capo_glue.types.create_job_response.CreateJobResponse:
    out: capo_glue.types.create_job_response.CreateJobResponse = (
        capo_glue.types.create_job_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> capo_glue.types.create_job_response.CreateJobResponse:
    out: capo_glue.types.create_job_response.CreateJobResponse = (
        capo_glue.types.create_job_response.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> capo_glue._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or capo_glue._auth._sigv4.build_sigv4_auth_scheme("glue", options.region)
        )
        if sigv4_config is not None:
            return capo_glue._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: capo_glue.types.create_job_request.CreateJobRequest,
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
    headers["X-Amz-Target"] = "AWSGlue.CreateJob"
    body: bytes | None = json.dumps(
        capo_glue.types.create_job_request.serialize_aws_json_1_1(input_)
    ).encode()
    headers["content-type"] = "application/x-amz-json-1.1"
    signer = get_signer(options, auth_schemes=endpoint.properties.get("authSchemes"))
    normalized_url = zapros.URL(url)
    normalized_url.search_params.update(params)
    return zapros.Request(
        normalized_url, "POST", headers=headers, body=body, context={"signer": signer}
    )


def create_job(
    options: OperationOptions,
    input_: capo_glue.types.create_job_request.CreateJobRequest,
) -> tuple[capo_glue.types.create_job_response.CreateJobResponse, zapros.Response]:
    response = options.client.handler.handle(build_request(options, input_))
    try:
        if response.status >= 400:
            response.read()
            handle_error(response)
        return handle_response(response), response
    except BaseException:
        response.close()
        raise


async def async_create_job(
    options: AsyncOperationOptions,
    input_: capo_glue.types.create_job_request.CreateJobRequest,
) -> tuple[capo_glue.types.create_job_response.CreateJobResponse, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
