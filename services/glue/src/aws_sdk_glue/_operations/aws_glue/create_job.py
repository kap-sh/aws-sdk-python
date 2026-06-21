"""Generated from Smithy shape ``com.amazonaws.glue#CreateJob``."""

from __future__ import annotations

import json
from typing import Any

import zapros
from typing_extensions import Never

import aws_sdk_glue._auth._signers
import aws_sdk_glue._auth._sigv4
import aws_sdk_glue.errors.already_exists_exception
import aws_sdk_glue.errors.concurrent_modification_exception
import aws_sdk_glue.errors.idempotent_parameter_mismatch_exception
import aws_sdk_glue.errors.internal_service_exception
import aws_sdk_glue.errors.invalid_input_exception
import aws_sdk_glue.errors.operation_timeout_exception
import aws_sdk_glue.errors.resource_number_limit_exceeded_exception
import aws_sdk_glue.types.code_gen_configuration_nodes
import aws_sdk_glue.types.connections_list
import aws_sdk_glue.types.create_job_request
import aws_sdk_glue.types.create_job_response
import aws_sdk_glue.types.execution_class
import aws_sdk_glue.types.execution_property
import aws_sdk_glue.types.generic_map
import aws_sdk_glue.types.job_command
import aws_sdk_glue.types.job_mode
import aws_sdk_glue.types.notification_property
import aws_sdk_glue.types.source_control_details
import aws_sdk_glue.types.tags_map
import aws_sdk_glue.types.worker_type
from aws_sdk_glue._protocol.errors import parse_error_metadata_json
from aws_sdk_glue._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_glue._services._pipeline import AsyncOperationOptions, OperationOptions
from aws_sdk_glue.errors import UnknownServiceError


def handle_error(response: zapros.Response) -> Never:
    data = json.loads(response.read())
    code, message = parse_error_metadata_json(response, data)
    match code:
        case "AlreadyExistsException":
            raise aws_sdk_glue.errors.already_exists_exception.AlreadyExistsException.from_aws_json_1_1(
                data
            )
        case "ConcurrentModificationException":
            raise aws_sdk_glue.errors.concurrent_modification_exception.ConcurrentModificationException.from_aws_json_1_1(
                data
            )
        case "IdempotentParameterMismatchException":
            raise aws_sdk_glue.errors.idempotent_parameter_mismatch_exception.IdempotentParameterMismatchException.from_aws_json_1_1(
                data
            )
        case "InternalServiceException":
            raise aws_sdk_glue.errors.internal_service_exception.InternalServiceException.from_aws_json_1_1(
                data
            )
        case "InvalidInputException":
            raise aws_sdk_glue.errors.invalid_input_exception.InvalidInputException.from_aws_json_1_1(
                data
            )
        case "OperationTimeoutException":
            raise aws_sdk_glue.errors.operation_timeout_exception.OperationTimeoutException.from_aws_json_1_1(
                data
            )
        case "ResourceNumberLimitExceededException":
            raise aws_sdk_glue.errors.resource_number_limit_exceeded_exception.ResourceNumberLimitExceededException.from_aws_json_1_1(
                data
            )
        case _:
            raise UnknownServiceError(code=code, message=message, response=response)


def handle_response(
    response: zapros.Response,
) -> aws_sdk_glue.types.create_job_response.CreateJobResponse:
    out: aws_sdk_glue.types.create_job_response.CreateJobResponse = (
        aws_sdk_glue.types.create_job_response.deserialize_aws_json_1_1(
            json.loads(response.read())
        )
    )
    return out


async def async_handle_response(
    response: zapros.Response,
) -> aws_sdk_glue.types.create_job_response.CreateJobResponse:
    out: aws_sdk_glue.types.create_job_response.CreateJobResponse = (
        aws_sdk_glue.types.create_job_response.deserialize_aws_json_1_1(
            json.loads(await response.aread())
        )
    )
    return out


def get_signer(
    options: AsyncOperationOptions | OperationOptions,
    auth_schemes: list[dict[str, Any]] | None = None,
) -> aws_sdk_glue._auth._signers.Signer | None:
    name_to_schema = {s["name"]: s for s in (auth_schemes or [])}  # noqa: F841
    if options.credentials_provider is not None:
        sigv4_config = (
            name_to_schema.get("sigv4")
            or name_to_schema.get("sigv4a")
            or name_to_schema.get("sigv4-s3express")
            or aws_sdk_glue._auth._sigv4.build_sigv4_auth_scheme("glue", options.region)
        )
        if sigv4_config is not None:
            return aws_sdk_glue._auth._signers.SigV4Signer(
                options.credentials_provider, auth_scheme=sigv4_config
            )
    raise RuntimeError("Auth was not resolved")


def build_request(
    options: OperationOptions | AsyncOperationOptions,
    input_: aws_sdk_glue.types.create_job_request.CreateJobRequest,
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
    import aws_sdk_glue.types.create_job_request

    body: bytes | None = json.dumps(
        aws_sdk_glue.types.create_job_request.serialize_aws_json_1_1(input_)
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
    input_: aws_sdk_glue.types.create_job_request.CreateJobRequest,
) -> tuple[aws_sdk_glue.types.create_job_response.CreateJobResponse, zapros.Response]:
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
    input_: aws_sdk_glue.types.create_job_request.CreateJobRequest,
) -> tuple[aws_sdk_glue.types.create_job_response.CreateJobResponse, zapros.Response]:
    response = await options.client.handler.ahandle(build_request(options, input_))
    try:
        if response.status >= 400:
            await response.aread()
            handle_error(response)
        return await async_handle_response(response), response
    except BaseException:
        await response.aclose()
        raise
